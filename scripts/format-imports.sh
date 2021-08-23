#!/bin/sh -e
set -x

isort hqme tests scripts --force-single-line-imports
sh ./scripts/format.sh