#!/usr/bin/env sh

# Ignore "E501 - line too long" errors
pycodestyle --show-source --show-pep8 --statistics --ignore=E501,W504,W503 .
