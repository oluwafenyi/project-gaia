from .base import *

import dj_database_url


DEBUG = True


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    *MIDDLEWARE
]


ALLOWED_HOSTS = [
    '.herokuapp.com'
]


DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = 'gaia-bucket'

AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)

AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'config.storage_backends.MediaStorage'
