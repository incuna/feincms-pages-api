#! /usr/bin/env python
"""From http://stackoverflow.com/a/12260597/400691"""
import sys

import dj_database_url
import django
from colour_runner.django_runner import ColourRunnerMixin
from django.conf import settings


settings.configure(
    DATABASES={
        'default': dj_database_url.config(default='postgres://localhost/pages'),
    },
    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    INSTALLED_APPS=(
        'pages',
        'pages.tests',  # This adds the test User model.

        # 3rd party app
        'feincms',
        'user_management.api',

        # Put contenttypes before auth to work around test issue.
        # See: https://code.djangoproject.com/ticket/10827#comment:12
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.admin',
    ),
    MIDDLEWARE_CLASSES=(),
    PASSWORD_HASHERS=('django.contrib.auth.hashers.MD5PasswordHasher',),
    SITE_ID=1,
    AUTH_USER_MODEL='tests.User',
    ROOT_URLCONF='pages.tests.urls',
)


if django.VERSION >= (1, 7):
    django.setup()


# DiscoverRunner requires `django.setup()` to have been called
from django.test.runner import DiscoverRunner  # noqa


class TestRunner(ColourRunnerMixin, DiscoverRunner):
    """Enable colorised output."""

test_runner = TestRunner(verbosity=1)
failures = test_runner.run_tests(['pages'])
if failures:
    sys.exit(1)
