#!/usr/bin/env bash
set -euo pipefail

# install_deps.sh for code/docker
cd /workspace || exit 1

# Force reinstall: remove marker at container start so installation always runs.
MARKER_FILE="/workspace/.deps_installed"
if [ -f "${MARKER_FILE}" ]; then
  echo "Removing existing marker ${MARKER_FILE} to force dependency reinstall on startup."
  rm -f "${MARKER_FILE}" || true
fi

# If marker removal is desired to be conditional, set SKIP_INSTALL=1 to skip installation entirely.
if [ -n "${SKIP_INSTALL:-}" ]; then
  echo "SKIP_INSTALL set; skipping dependency installation."
  # If a command was provided, run it; otherwise drop to bash
  if [ "$#" -gt 0 ]; then
    exec "$@"
  else
    exec bash
  fi
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

# After installation, run the provided command so container keeps running.
if [ "$#" -gt 0 ]; then
  exec "$@"
else
  exec bash
fi
