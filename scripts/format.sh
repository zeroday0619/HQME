#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place hqme tests scripts --exclude=__init__.py
black hqme tests scripts
isort hqme tests scripts