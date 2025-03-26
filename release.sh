#!/bin/bash
set -o errexit
set -o pipefail

# Run tests before release
#tox -p 4

# Bump up major version number
.poetry/bin/poetry version minor
VERSION="v$(.poetry/bin/poetry version -s)"

# Commit new version number and create a tag and Github release
git add pyproject.toml && git commit -am "Bump up version number to v$(.poetry/bin/poetry version -s)"
git tag $VERSION
git push
git push --tags
gh release create --generate-notes --latest --title=$VERSION $VERSION

# Publish to Pypi
.poetry/bin/poetry publish --build
