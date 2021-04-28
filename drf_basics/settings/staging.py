from drf_basics.settings.base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'staging_db_name',
        'USER': 'staging_username',
        'PASSWORD': 'staging_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
