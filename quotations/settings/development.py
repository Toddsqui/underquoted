from quotations.settings.common import *

import os

SECRET_KEY = 'oe3-zo6yeb34h*ktvana^ejbb(^du)613z+tl8@)psqkr+k7sd'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quotations',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_ROOT = '/tmp/static'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

MEDIA_ROOT = '/tmp/media'

ALLOWED_HOSTS = ['*']

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
