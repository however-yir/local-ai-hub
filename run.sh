#!/bin/bash

image_name="local-ai-hub"
container_name="local-ai-hub"
host_port=3000
container_port=8080

docker build -t "$image_name" .
docker stop "$container_name" &>/dev/null || true
docker rm "$container_name" &>/dev/null || true

env_file_arg=()
if [ -f ".env.local" ]; then
    env_file_arg=(--env-file ".env.local")
elif [ -f ".env" ]; then
    env_file_arg=(--env-file ".env")
fi

docker run -d -p "$host_port":"$container_port" \
    --add-host=host.docker.internal:host-gateway \
    "${env_file_arg[@]}" \
    -v "${image_name}:/app/backend/data" \
    --name "$container_name" \
    --restart always \
    "$image_name"

docker image prune -f
