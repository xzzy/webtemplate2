#!/usr/bin/env python

import os
import sys
from django.conf import settings
import django


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
# Minimal Django settings to provide an auth-ready project, plus staticfiles.
DEFAULT_SETTINGS = dict(
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'webtemplate_dpaw',
    ),
    DATABASES={
        'default': {'ENGINE': 'django.db.backends.sqlite3'}
    },
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
    ),
    ROOT_URLCONF='webtemplate_dpaw.tests.urls',
    STATIC_URL='/static/',
    ANONYMOUS_USER_ID=-1,
    TEMPLATE_DIRS=(os.path.join(BASE_DIR, 'webtemplate_dpaw', 'tests'),),
)


def runtests():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)

    django.setup()

    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    try:
        from django.test.runner import DiscoverRunner
        runner_class = DiscoverRunner
        test_args = ['webtemplate_dpaw.tests']
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner
        runner_class = DjangoTestSuiteRunner
        test_args = ['webtemplate_dpaw.tests']

    failures = runner_class(
        verbosity=2, interactive=True, failfast=True).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
