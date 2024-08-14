"""
WSGI config for proj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .flask_app import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

# application = get_wsgi_application()
app = create_app()
application = app.wsgi_app  # get_wsgi_application()
