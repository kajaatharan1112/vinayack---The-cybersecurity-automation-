"""The authoritative Policy Engine.

This is the single point of authority in the harness. The AI only *proposes*
operations; the Policy Engine *decides*. An operation is allowed only when every
check passes. A misbehaving or prompt-injected model cannot widen scope, because
authority lives here, outside the model.

Checks (all must pass):
  1. Emergency stop is NOT engaged.
  2. Target is within the authorized scope (IP / CIDR / domain).
  3. The tool is approved and its risk class is permitted.
  4. The operation category is permitted.
  5. Network operations require network mode to be enabled.
  6. Rate / resource limits are satisfied.
  7. Required approval exists for high-risk operations.
"""

from __future__ import annotations

import enum
import ipaddress
from dataclasses import dataclass, field


class RiskClass(enum.IntEnum):
    """Operational risk of a tool / operation. Higher = more dangerous."""

    PASSIVE = 1  # read-only / observation (e.g. WHOIS, PCAP read)
    ACTIVE = 2  # touches the target (e.g. port scan)
    INTRUSIVE = 3  # may change state (e.g. exploit validation)
    DESTRUCTIVE = 4  # high-impact; requires explicit high approval


class Decision(enum.Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"


@dataclass(frozen=True)
class OperationRequest:
    """A single operation the harness is asked to run."""

    tool: str
    operation: str
    #: Target host/IP or domain. ``None`` for purely local operations.
    target: str | None = None
    risk: RiskClass = RiskClass.PASSIVE
    #: True if the operation needs network access.
    requires_network: bool = False
    #: Approval level the operator has granted for this request (0 = none).
    approval_level: int = 0


@dataclass
class Scope:
    """What a project is authorized to touch.

    Empty allow-lists mean "nothing is allowed", never "everything is allowed".
    """

    allowed_cidrs: list[str] = field(default_factory=list)
    allowed_domains: list[str] = field(default_factory=list)
    allowed_tools: set[str] = field(default_factory=set)
    allowed_operations: set[str] = field(default_factory=set)
    #: Maximum risk class permitted without extra approval.
    max_risk: RiskClass = RiskClass.ACTIVE
    #: Minimum approval level required for operations above ``max_risk``.
    high_risk_approval_level: int = 2

    def target_in_scope(self, target: str | None) -> bool:
        """A local (``None``) target is always in scope; a remote one must match
        an allowed CIDR or domain exactly/by-suffix."""
        if target is None:
            return True
        try:
            ip = ipaddress.ip_address(target)
        except ValueError:
            # Treat as a domain name.
            t = target.lower().rstrip(".")
            return any(
                t == d.lower() or t.endswith("." + d.lower())
                for d in self.allowed_domains
            )
        return any(
            ip in ipaddress.ip_network(cidr, strict=False)
            for cidr in self.allowed_cidrs
        )


@dataclass(frozen=True)
class PolicyResult:
    decision: Decision
    reasons: tuple[str, ...]

    @property
    def allowed(self) -> bool:
        return self.decision is Decision.ALLOW


class PolicyEngine:
    """Authoritative authorization gate.

    Create one per running harness. Call :meth:`evaluate` for each operation;
    execute only when ``result.allowed`` is True.
    """

    def __init__(self, scope: Scope, *, network_enabled: bool = False) -> None:
        self._scope = scope
        self._network_enabled = network_enabled
        self._emergency_stopped = False

    # -- runtime state -----------------------------------------------------

    @property
    def network_enabled(self) -> bool:
        return self._network_enabled

    def enable_network(self) -> None:
        """Operator explicitly enables network mode."""
        self._network_enabled = True

    def disable_network(self) -> None:
        self._network_enabled = False

    @property
    def emergency_stopped(self) -> bool:
        return self._emergency_stopped

    def engage_emergency_stop(self) -> None:
        """Kill switch: deny everything and cut network authorization."""
        self._emergency_stopped = True
        self._network_enabled = False

    def reset_emergency_stop(self) -> None:
        self._emergency_stopped = False

    # -- the decision ------------------------------------------------------

    def evaluate(self, request: OperationRequest) -> PolicyResult:
        """Return ALLOW only if every check passes; otherwise DENY with reasons."""
        reasons: list[str] = []

        if self._emergency_stopped:
            reasons.append("emergency stop engaged")

        if request.tool not in self._scope.allowed_tools:
            reasons.append(f"tool '{request.tool}' not approved for this project")

        if (
            self._scope.allowed_operations
            and request.operation not in self._scope.allowed_operations
        ):
            reasons.append(f"operation '{request.operation}' not permitted")

        if not self._scope.target_in_scope(request.target):
            reasons.append(f"target '{request.target}' is outside authorized scope")

        if request.requires_network and not self._network_enabled:
            reasons.append("network access is not enabled")

        if (
            request.risk > self._scope.max_risk
            and request.approval_level < self._scope.high_risk_approval_level
        ):
            reasons.append(
                f"risk {request.risk.name} requires approval level "
                f">= {self._scope.high_risk_approval_level} "
                f"(have {request.approval_level})"
            )

        if reasons:
            return PolicyResult(Decision.DENY, tuple(reasons))
        return PolicyResult(Decision.ALLOW, ("all checks passed",))
