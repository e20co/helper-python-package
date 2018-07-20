#!/usr/bin/env sh

coverage run -m unittest discover tests

# Limit the coverage to own files
coverage report --include="helper_python/*" -m
coverage erase
