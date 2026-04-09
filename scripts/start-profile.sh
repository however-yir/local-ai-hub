#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ENV_FILE="${ROOT_DIR}/.env"
ENV_LOCAL_EXAMPLE="${ROOT_DIR}/.env.local.example"
ENV_PROD_EXAMPLE="${ROOT_DIR}/.env.production.example"

usage() {
  cat <<'USAGE'
Usage: ./scripts/start-profile.sh <profile>

Profiles:
  with-ollama   Start Open WebUI + Redis + Ollama in local compose
  no-ollama     Start Open WebUI + Redis only (uses external OLLAMA_BASE_URL)
  prod-redis    Start Open WebUI only (uses external REDIS_URL and OLLAMA_BASE_URL)
USAGE
}

ensure_env() {
  if [[ ! -f "${ENV_FILE}" ]]; then
    cp "${ENV_LOCAL_EXAMPLE}" "${ENV_FILE}"
    echo "Created ${ENV_FILE} from ${ENV_LOCAL_EXAMPLE}."
  fi
}

profile="${1:-}"
if [[ -z "${profile}" ]]; then
  usage
  exit 1
fi

ensure_env

case "${profile}" in
  with-ollama)
    docker compose --env-file "${ENV_FILE}" -f "${ROOT_DIR}/docker-compose.yaml" up -d --build
    ;;
  no-ollama)
    docker compose --env-file "${ENV_FILE}" -f "${ROOT_DIR}/docker-compose.yaml" up -d redis
    docker compose --env-file "${ENV_FILE}" -f "${ROOT_DIR}/docker-compose.yaml" up -d --no-deps open-webui
    ;;
  prod-redis)
    if grep -q "redis://redis:6379/0" "${ENV_FILE}"; then
      echo "Please set external REDIS_URL in ${ENV_FILE} (you can start from .env.production.example)." >&2
      exit 1
    fi
    docker compose --env-file "${ENV_FILE}" -f "${ROOT_DIR}/docker-compose.yaml" up -d --no-deps open-webui
    ;;
  *)
    usage
    exit 1
    ;;
esac

echo "Profile '${profile}' started."
