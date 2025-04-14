#!/usr/bin/env bash
#
# This file is for launching the application in the container
#

# shellcheck disable=SC2039
set -exuo pipefail

# Using PORT if defined (in Google Cloud Run), defaulting to 8000
export PORT=${PORT:-8000}

set -- poetry run serve
exec "$@"
