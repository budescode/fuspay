from .settings import *
import os
DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
STATIC_URL = '/static/'
STATIC_ROOT =  os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media_cdn/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media_cdn')