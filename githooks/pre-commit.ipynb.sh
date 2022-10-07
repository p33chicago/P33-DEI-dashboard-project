#!/usr/bin/env sh

# Clear notebook outputs
changed=$(git diff --name-only --cached notebooks/*.ipynb)
if [ -z $changed ]; then
  exit 0
fi
echo "Removing notebook output from $changed"
echo $changed | xargs jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace
echo $changed | xargs git add
