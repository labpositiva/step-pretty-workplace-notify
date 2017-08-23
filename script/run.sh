#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# shellcheck source=/dev/null
[ -r "script/bootstrap.sh" ] && source "script/bootstrap.sh"

cd "${ROOT_DIR}" || echo 'Not Found'

if [ "$1" == "" ]; then
    docker-compose up --remove-orphans
elif [ "$1" == "dev" ]; then
    docker-compose -f docker-compose.yml -f docker-compose/dev.yml -p "${PROJECT_NAME_DEV}" run --rm app "${2}"
elif [ "$1" == "test" ]; then
    docker-compose -f docker-compose.yml -f docker-compose/test.yml -p "${PROJECT_NAME_TEST}" run --rm app "${2}"
elif [ "$1" == "prod" ]; then
    docker-compose -f docker-compose.yml -f docker-compose/prod.yml -p "${PROJECT_NAME}" run --rm app "${2}"
fi