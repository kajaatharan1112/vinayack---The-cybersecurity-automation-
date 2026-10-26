"""Tool catalog, manager, and integration layer.

This package turns the owner's study notes (``notes/01_Kali_Tools``) and a set of
curated open-source extras into a structured, policy-aware tool catalog, probes
which tools are actually installed, and performs *safe, gated* updates. Nothing
here runs a security tool against a target; that remains the Policy Engine's and
the Job Engine's job. This layer only answers "what tools exist, are they
installed, and how do we keep them current".
"""

from harness.tools.catalog import CatalogEntry, ToolCatalog, load_catalog
from harness.tools.manager import SyncPlan, SyncStep, ToolManager, ToolStatus

__all__ = [
    "CatalogEntry",
    "ToolCatalog",
    "load_catalog",
    "ToolManager",
    "ToolStatus",
    "SyncPlan",
    "SyncStep",
]
