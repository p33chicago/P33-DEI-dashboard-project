#!/usr/bin/env sh

# Process data and start dev server

set -e

PYTHON="${PYTHON:-$(which python)}"
WEB="${WEB:-web}"

$PYTHON build.py
(cd $WEB && npm run dev)
