
from .base import *


DEBUG = True


ALLOWED_HOSTS = []


INSTALLED_APPS += [
    'django_extensions',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
