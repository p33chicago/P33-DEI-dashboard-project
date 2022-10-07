#!/usr/bin/env sh

# Process data and start dev server

set -e

pip install -r requirements.txt
(
  cd web &&
    npm install &&
    npx playwright install
)
