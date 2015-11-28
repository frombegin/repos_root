#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .common import *


# DEBUG
# ------------------------------------------------------------------------------
DEBUG_APPS = (
    'debug_toolbar',
)

INSTALLED_APPS += DEBUG_APPS

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
