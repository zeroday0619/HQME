#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place docs_src hqme tests scripts --exclude=__init__.py
black hqme tests docs_src scripts
isort hqme tests docs_src scripts