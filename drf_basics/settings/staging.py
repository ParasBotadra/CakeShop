from drf_basics.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['68.183.80.25']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
