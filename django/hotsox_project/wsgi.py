"""
WSGI config for hotsox_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings
from .utilities import create_db_entry_social_app


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotsox_project.settings")

application = get_wsgi_application()

# Hook in here to create defaults for AllAuth in the database
# make sure google is stored in the socialaccount apps in the database
# set SITE_ID from the entry of database
created, settings.SITE_ID = create_db_entry_social_app(
    site_name="127.0.0.1:8000",
    site_domain="127.0.0.1:8000",
    provider="google",
    name="Google",
    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
    secret=os.environ.get("GOOGLE_SECRET"),
)
if created:
    print("included google to AllAuth, set SITE_ID to:", settings.SITE_ID)
