#!/usr/bin/env bash
set -euo pipefail

# install_deps.sh for code/docker
cd /workspace || exit 1

# If marker exists and not forced, skip installation to speed up container startup.
MARKER_FILE="/workspace/.deps_installed"
FORCE_INSTALL=${FORCE_REINSTALL:-""}
if [ -f "${MARKER_FILE}" ] && [ -z "${FORCE_INSTALL}" ]; then
  echo "Dependencies already installed (marker ${MARKER_FILE} exists). Skipping installation."
  exit 0
fi

# If we get here, perform installation (or forced reinstall)

echo "Updating pip/setuptools/wheel..."
python -m pip install --upgrade pip setuptools wheel

# Run detector to generate requirements_auto.txt
if [ -x "/usr/local/bin/detect_deps.py" ]; then
  echo "Detecting dependencies..."
  /usr/local/bin/detect_deps.py || true
else
  # fallback to local path in case container copies differently
  if [ -f ./docker/detect_deps.py ]; then
    echo "Detecting dependencies using ./docker/detect_deps.py..."
    python ./docker/detect_deps.py || true
  else
    echo "Warning: detector not found. Skipping detection."
  fi
fi

REQ_FILE=""
if [ -f requirements.txt ]; then
  REQ_FILE=requirements.txt
elif [ -s requirements_auto.txt ]; then
  REQ_FILE=requirements_auto.txt
fi

if [ -n "${REQ_FILE}" ]; then
  echo "Installing Python packages from ${REQ_FILE}..."
  # Try grouped install first; if it fails, attempt per-package installs to be resilient
  if ! python -m pip install -r "${REQ_FILE}"; then
    echo "Grouped pip install failed; attempting per-package installation..."
    while IFS= read -r pkg || [ -n "$pkg" ]; do
      # skip empty/comment lines
      case "$pkg" in
        ''|\#*) continue ;;
      esac
      echo "Installing ${pkg}..."
      python -m pip install "${pkg}" || echo "Warning: failed to install ${pkg}, continuing"
    done < "${REQ_FILE}"
  fi
elif [ -f pyproject.toml ]; then
  echo "pyproject.toml found; attempting to install package (pip install .)"
  python -m pip install . || echo "pip install . failed, please check pyproject.toml"
else
  echo "No requirements.txt, requirements_auto.txt, or pyproject.toml found. Skipping pip install."
fi

# Optional: show installed packages
python -m pip freeze | sed -n '1,200p'

# Ensure 'requests' is importable; if not, attempt to install it (fallback)
python - <<'PY'
import sys
try:
    import requests
    print('requests is available')
except Exception:
    print('requests not found; attempting to install requests...')
    try:
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
        print('requests installed successfully')
    except Exception as e:
        print('Failed to install requests:', e)
PY

# Mark installation complete
touch "${MARKER_FILE}"
echo "Dependency installation complete. Marker created at ${MARKER_FILE}."
