# -*- coding: utf-8 -*-

import os

# Wercker git

WERCKER_STEP_ROOT = os.environ.get('WERCKER_STEP_ROOT')

WERCKER_PRETTY_WORKPLACE_TOKEN = os.environ.get(
    'WERCKER_PRETTY_WORKPLACE_TOKEN'
)
WERCKER_PRETTY_WORKPLACE_GROUP = os.environ.get(
    'WERCKER_PRETTY_WORKPLACE_GROUP'
)
WERCKER_PRETTY_WORKPLACE_NOTIFY_ON = os.environ.get(
    'WERCKER_PRETTY_WORKPLACE_NOTIFY_ON'
)
WERCKER_PRETTY_WORKPLACE_BRANCHES = os.environ.get(
    'WERCKER_PRETTY_WORKPLACE_BRANCHES'
)
WERCKER_PRETTY_WORKPLACE_PASSED_MESSAGE = os.environ.get(
    'WERCKER_PRETTY_WORKPLACE_PASSED_MESSAGE'
)
WERCKER_PRETTY_WORKPLACE_FAILED_MESSAGE = os.environ.get(
    'WERCKER_PRETTY_WORKPLACE_FAILED_MESSAGE'
)

WERCKER_APPLICATION_URL = os.environ.get('WERCKER_APPLICATION_URL')
WERCKER_BUILD_URL = os.environ.get('WERCKER_BUILD_URL')
WERCKER_RUN_URL = os.environ.get('WERCKER_RUN_URL')

# Wercker git
WERCKER_GIT_OWNER = os.environ.get('WERCKER_GIT_OWNER')
WERCKER_GIT_REPOSITORY = os.environ.get('WERCKER_GIT_REPOSITORY')
WERCKER_GIT_COMMIT = os.environ.get('WERCKER_GIT_COMMIT')
WERCKER_GIT_BRANCH = os.environ.get('WERCKER_GIT_BRANCH')
WERCKER_GIT_DOMAIN = os.environ.get('WERCKER_GIT_DOMAIN')
WERCKER_STARTED_BY = os.environ.get('WERCKER_STARTED_BY')

DEPLOY = os.environ.get('DEPLOY')
# DEPLOY=true

WERCKER_DEPLOY_URL = os.environ.get('WERCKER_DEPLOY_URL')
WERCKER_DEPLOYTARGET_NAME = os.environ.get('WERCKER_DEPLOYTARGET_NAME')

# WERCKER_RESULT=passed
WERCKER_RESULT = os.environ.get('WERCKER_RESULT')
