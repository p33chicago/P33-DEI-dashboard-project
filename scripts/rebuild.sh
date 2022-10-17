#!/usr/bin/env sh

# Regenerate data and copy to web directory

# WARNING: if you're not using the development web server, and are instead
#  previewing the compiled version of the site, you'll need to recompile
# after running this command

set -e

python build.py
(cd web && npm run copy-data)
