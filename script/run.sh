#!/usr/bin/env bash
# -*- coding: utf-8 -*-

# shellcheck source=/dev/null
[ -r "script/bootstrap.sh" ] && source "script/bootstrap.sh"

cd "${ROOT_DIR}" || echo 'Not Found'

if [ ! -n "$WERCKER_TOKEN" ]; then
  fail 'Please specify Token'
fi

if [ ! -n "$WERCKER_GROUP" ]; then
  fail 'Please specify Group'
fi

if [ "$WERCKER_WORKPLACE_NOTIFY_ON" = "failed" ]; then
  if [ "$WERCKER_RESULT" = "passed" ]; then
    echo "Skipping.."
    return 0
  fi
fi

if [ -n "$WERCKER_WORKPLACE_NOTIFY_BRANCH" ]; then
  if [ "$WERCKER_GIT_BRANCH" != "$WERCKER_WORKPLACE_NOTIFY_BRANCH" ]; then
    echo "Workplace notification not necessary on this branch. Skipping.."
    return 0
  fi
fi

python "${SOURCE_DIR}/run.py"