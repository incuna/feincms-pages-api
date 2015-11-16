SECRET_KEY = 'not-for-production'

INSTALLED_APPS = (
    'pages',
    'pages.tests',

    # 3rd party app
    'feincms',
    'user_management.api',

    # Put contenttypes before auth to work around test issue.
    # See: https://code.djangoproject.com/ticket/10827#comment:12
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.admin',
)

AUTH_USER_MODEL = 'tests.User'

MIGRATION_MODULES = {
    'api': 'pages.tests.testmigrations.api',
    'pages': 'pages.tests.testmigrations.pages',
    'feincms': 'pages.tests.testmigrations.feincms',
}
