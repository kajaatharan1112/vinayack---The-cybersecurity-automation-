#!/usr/bin/env bash
# Thin wrapper around scripts/update_tools.py (the one-click tool updater).
# Usage: scripts/update_tools.sh [--network] [--execute] [--only nmap tshark]
set -euo pipefail
cd "$(dirname "$0")/.."
exec python3 scripts/update_tools.py "$@"
