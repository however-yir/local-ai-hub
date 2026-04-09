#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [ ! -x "node_modules/.bin/eslint" ] || [ ! -x "node_modules/.bin/svelte-kit" ]; then
  echo "Bootstrapping frontend dev dependencies via npm ci..."
  npm ci --force
fi

TOOLS_VENV=".cache/dev-tools"
PYLINT_BIN="$TOOLS_VENV/bin/pylint"

if [ ! -x "$PYLINT_BIN" ]; then
  echo "Bootstrapping Python lint tools in $TOOLS_VENV..."
  python3 -m venv "$TOOLS_VENV"
  "$TOOLS_VENV/bin/python" -m pip install --disable-pip-version-check --quiet --upgrade pip
  "$TOOLS_VENV/bin/python" -m pip install --disable-pip-version-check --quiet pylint
fi
