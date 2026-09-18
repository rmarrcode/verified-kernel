#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/../.venv"

if [[ ! -x "${VENV_DIR}/bin/python" ]]; then
  echo "error: expected virtualenv Python at ${VENV_DIR}/bin/python" >&2
  exit 1
fi

cd "${SCRIPT_DIR}"

exec "${VENV_DIR}/bin/python" -m pytest tests "$@"
