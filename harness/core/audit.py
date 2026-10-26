"""Append-only audit log.

Every significant action in the harness is recorded here. The log is append-only
by contract: entries can be added and read, never mutated or removed. This backs
the project's transparency + audit non-negotiable.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class AuditEvent:
    """A single immutable audit record."""

    action: str
    #: Free-form details about the action (target, tool, decision, ...).
    details: dict[str, Any] = field(default_factory=dict)
    #: Unix timestamp (seconds). Injected automatically.
    timestamp: float = field(default_factory=time.time)
    #: Who/what initiated the action.
    actor: str = "system"

    def to_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True, default=str)


class AuditLog:
    """In-memory append-only audit log.

    A persistent (SQLite) backend will implement the same ``append`` / ``events``
    contract in a later phase; callers depend only on this interface.
    """

    def __init__(self) -> None:
        self._events: list[AuditEvent] = []

    def append(
        self,
        action: str,
        details: dict[str, Any] | None = None,
        actor: str = "system",
    ) -> AuditEvent:
        """Record an event and return it."""
        event = AuditEvent(action=action, details=details or {}, actor=actor)
        self._events.append(event)
        return event

    @property
    def events(self) -> tuple[AuditEvent, ...]:
        """Read-only view of all recorded events, in order."""
        return tuple(self._events)

    def find(self, action: str) -> list[AuditEvent]:
        """Return all events matching ``action``."""
        return [e for e in self._events if e.action == action]

    def __len__(self) -> int:
        return len(self._events)
