"""Offline-first harness lifecycle.

Implements the startup sequence from the master plan (§3.1): the harness comes up
OFFLINE, with network access disabled, and only transitions to network mode when
an operator explicitly authorizes it. Every transition is audited, and an
emergency stop can revoke everything instantly.
"""

from __future__ import annotations

from harness.core.audit import AuditLog
from harness.core.config import HarnessConfig, OperatingMode
from harness.core.policy import PolicyEngine, Scope


class Harness:
    """The running harness instance: config + policy + audit + mode."""

    def __init__(
        self,
        config: HarnessConfig | None = None,
        scope: Scope | None = None,
        audit: AuditLog | None = None,
    ) -> None:
        self.config = config or HarnessConfig()
        self.audit = audit or AuditLog()
        self.policy = PolicyEngine(
            scope or Scope(),
            network_enabled=self.config.network_enabled_by_default,
        )
        self._mode = self.config.start_mode
        self._started = False

    @property
    def mode(self) -> OperatingMode:
        return self._mode

    @property
    def started(self) -> bool:
        return self._started

    # -- startup -----------------------------------------------------------

    def start(self) -> None:
        """Run the offline-first startup sequence.

        The harness never initiates network communication during startup.
        """
        self.audit.append("harness.init", {"instance": self.config.instance_name})
        self.audit.append("policy.loaded")
        self.audit.append("registry.init")
        self._mode = OperatingMode.OFFLINE
        self._started = True
        self.audit.append("harness.offline_ready")

    # -- mode transitions --------------------------------------------------

    def enable_network(self, actor: str = "operator") -> None:
        """Operator authorizes network mode. Refused if emergency-stopped."""
        if self.policy.emergency_stopped:
            self.audit.append("network.enable_refused", {"reason": "emergency stop"})
            raise RuntimeError("cannot enable network while emergency stop is engaged")
        self.policy.enable_network()
        self._mode = OperatingMode.NETWORK_ENABLED
        self.audit.append("network.enabled", actor=actor)

    def disable_network(self, actor: str = "operator") -> None:
        self.policy.disable_network()
        self._mode = OperatingMode.OFFLINE
        self.audit.append("network.disabled", actor=actor)

    def emergency_stop(self, actor: str = "operator") -> None:
        """Kill switch: revoke network authorization and deny all operations."""
        self.policy.engage_emergency_stop()
        self._mode = OperatingMode.OFFLINE
        self.audit.append("emergency_stop.engaged", actor=actor)
