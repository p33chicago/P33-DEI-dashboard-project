#!/usr/bin/env sh

# Process data and start dev server

set -e

PIP="${PIP:-$(which pip)}"

$PIP install -r requirements.txt
(
  cd web &&
    npm install &&
    npx playwright install
)
