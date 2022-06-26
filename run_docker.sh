#!/bin/bash
set -euo pipefail

docker build -t dev-code-ex.backend -f ./docker/backend/Dockerfile . &
docker build -t dev-code-ex.frontend -f ./docker/frontend/Dockerfile . &

wait

docker-compose up -d