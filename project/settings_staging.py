from .settings import *
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST', 'db'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
STATIC_URL = '/static/'
STATIC_ROOT =  os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media_cdn/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media_cdn')