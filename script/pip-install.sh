#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# shellcheck source=/dev/null
[ -r "script/bootstrap.sh" ] && source "script/bootstrap.sh"

cd "${ROOT_DIR}" || echo 'Not Found'

if ! hash "${WERCKER_PIP_INSTALL_PIP_COMMAND}" 2>/dev/null; then
    fail "Pip command not found: ${WERCKER_PIP_INSTALL_PIP_COMMAND}"
fi
