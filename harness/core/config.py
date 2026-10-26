"""Harness configuration.

Defaults are deliberately the *safest* possible: the harness starts OFFLINE with
network access DISABLED and no elevated privileges. Everything must be turned on
explicitly by an authorized operator.
"""

from __future__ import annotations

import enum
from dataclasses import dataclass, field


class OperatingMode(enum.Enum):
    """The harness operating mode."""

    OFFLINE = "OFFLINE"
    NETWORK_ENABLED = "NETWORK_ENABLED"


@dataclass(frozen=True)
class HarnessConfig:
    """Immutable startup configuration.

    All network/privilege-bearing options default to the restrictive value so an
    un-configured harness can do nothing dangerous.
    """

    #: Human-readable name of the deployment.
    instance_name: str = "offline-harness"
    #: Where the local SQLite database lives (``:memory:`` for ephemeral/tests).
    database_path: str = ":memory:"
    #: Start in OFFLINE mode. Network must be enabled explicitly at runtime.
    start_mode: OperatingMode = OperatingMode.OFFLINE
    #: Network access is DISABLED until an operator authorizes it with a scope.
    network_enabled_by_default: bool = False
    #: The AI model adapter to load ("local_stub" keeps everything offline).
    model_adapter: str = "local_stub"
    #: Maximum concurrent running tasks.
    max_concurrent_tasks: int = 4
    #: Extra free-form settings for forward compatibility.
    extra: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.max_concurrent_tasks < 1:
            raise ValueError("max_concurrent_tasks must be >= 1")
