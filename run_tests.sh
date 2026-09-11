#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/../.venv"

if [[ ! -x "${VENV_DIR}/bin/python" ]]; then
  echo "error: expected virtualenv Python at ${VENV_DIR}/bin/python" >&2
  exit 1
fi

VENV_SITE_PACKAGES="$("${VENV_DIR}/bin/python" - <<'PY'
import sysconfig

print(sysconfig.get_paths()["purelib"])
PY
)"
VENV_CUDA_HOME="${VENV_SITE_PACKAGES}/nvidia/cu13"

if [[ -x "${VENV_CUDA_HOME}/bin/nvcc" ]]; then
  export CUDA_HOME="${VENV_CUDA_HOME}"
  export PATH="${CUDA_HOME}/bin:${PATH}"
  export LD_LIBRARY_PATH="${CUDA_HOME}/lib:${LD_LIBRARY_PATH:-}"
elif [[ -z "${CUDA_HOME:-}" || ! -x "${CUDA_HOME}/bin/nvcc" ]] && ! command -v nvcc >/dev/null 2>&1; then
  echo "error: nvcc was not found in ${VENV_CUDA_HOME}/bin, CUDA_HOME/bin, or PATH" >&2
  exit 1
fi

cd "${SCRIPT_DIR}"

"${VENV_DIR}/bin/python" - <<'PY'
import shutil

from torch.utils.cpp_extension import _get_build_directory

build_dir = _get_build_directory("verified_kernel_C", verbose=False)
shutil.rmtree(build_dir, ignore_errors=True)
PY

export VERIFIED_KERNEL_FORCE_REBUILD=1
"${VENV_DIR}/bin/python" - <<'PY'
from verified_kernel._extension import load_extension

load_extension()
PY

exec "${VENV_DIR}/bin/python" -m pytest tests "$@"
