#!/usr/bin/env bash

set -e
set -x

mypy hqme
flake8 hqme tests
black hqme tests --check
isort hqme tests scripts --check-only