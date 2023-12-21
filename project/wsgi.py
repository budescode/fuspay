"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
django_settings_module = os.environ.get('DJANGO_SETTINGS_MODULE', 'project.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_module)

application = get_wsgi_application()
