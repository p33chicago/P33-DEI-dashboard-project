#!/usr/bin/env sh

# Process data and start dev server

set -e

python build.py
(cd web && npm run dev)
