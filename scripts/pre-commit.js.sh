#!/usr/bin/env sh

# Run node's (npm) pre-commit system

set -e

changed=$(git diff --name-only --cached web/)
if [ -z $changed ]; then
  exit 0
fi
echo "Running pre-commit for web"
(cd web && npm run pre-commit)
