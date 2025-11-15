#!/usr/bin/env python3
"""
Scan the mounted /workspace for Python imports and produce a requirements_auto.txt
This is a heuristic: it extracts top-level module names from import statements and
filters out a minimal set of stdlib module names. The resulting names are written
one-per-line and can be used with pip install -r requirements_auto.txt.

Note: This is best-effort. If your project already has requirements.txt or
pyproject.toml, prefer using those.
"""
import os
import re

# Allow overriding the scan root (useful when running locally)
ROOT = os.environ.get('WORKSPACE_ROOT', '/workspace')
if not os.path.isdir(ROOT):
    ROOT = os.getcwd()
OUT = os.path.join(ROOT, 'requirements_auto.txt')

IMPORT_RE = re.compile(r'^(?:from\s+([\w\.]+)\s+import|import\s+([\w\.]+))')
STD_LIB = {
    # expanded common stdlib modules
    'sys','os','re','json','time','math','datetime','itertools','functools',
    'subprocess','threading','multiprocessing','http','urllib','email','hashlib',
    'typing','pathlib','logging','unittest','collections','enum','ssl','socket',
    'asyncio','gzip','importlib','io','random','concurrent','typing_extensions',
    'contextlib','base64','csv','heapq','inspect','pkgutil','shutil','signal',
}

# Known non-pypi names or project-internal helper module names to ignore
BLACKLIST = {
    'commons_func', 'common', 'utils', 'helpers', 'leadbest', 'run_tasks',
}

found = set()

def is_local_module(root, name):
    """Return True if 'name' appears to be a local module/package in the repo."""
    # check for file or package at repository root
    candidate_file = os.path.join(root, f"{name}.py")
    candidate_pkg = os.path.join(root, name)
    if os.path.isfile(candidate_file):
        return True
    if os.path.isdir(candidate_pkg) and os.path.isfile(os.path.join(candidate_pkg, '__init__.py')):
        return True
    # also search anywhere under root for a matching file (expensive but safe)
    for dirpath, dirnames, filenames in os.walk(root):
        if f"{name}.py" in filenames:
            return True
        if name in dirnames and os.path.isfile(os.path.join(dirpath, name, '__init__.py')):
            return True
    return False

for dirpath, dirnames, filenames in os.walk(ROOT):
    # skip virtualenvs or hidden .git
    if '/.git' in dirpath or 'venv' in dirpath or '.venv' in dirpath:
        continue
    for fn in filenames:
        if not fn.endswith('.py'):
            continue
        fp = os.path.join(dirpath, fn)
        try:
            with open(fp, 'r', encoding='utf-8') as f:
                for line in f:
                    m = IMPORT_RE.match(line.strip())
                    if m:
                        mod = m.group(1) or m.group(2)
                        if not mod:
                            continue
                        top = mod.split('.')[0]
                        if not top:
                            continue
                        # filter stdlib, private modules, blacklist, and local modules
                        if top in STD_LIB:
                            continue
                        if top.startswith('_'):
                            continue
                        if top in BLACKLIST:
                            continue
                        if is_local_module(ROOT, top):
                            # skip modules that are part of this repository
                            continue
                        found.add(top)
        except Exception:
            # ignore unreadable files
            continue

# simple mapping for common name differences
MAPPING = {
    'bs4': 'beautifulsoup4',
    'PIL': 'Pillow',
    'yaml': 'PyYAML',
    'cv2': 'opencv-python',
    'jwt': 'PyJWT',
}

final = set()
for pkg in sorted(found):
    final.add(MAPPING.get(pkg, pkg))

# write output
if final:
    with open(OUT, 'w', encoding='utf-8') as f:
        for pkg in sorted(final):
            f.write(pkg + '\n')
    print(f'Wrote {len(final)} packages to {OUT}')
else:
    # touch an empty file to indicate nothing found
    open(OUT, 'w', encoding='utf-8').close()
    print('No third-party imports detected; created empty requirements_auto.txt')
