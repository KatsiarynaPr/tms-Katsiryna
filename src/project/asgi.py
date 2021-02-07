"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from api.main import app

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_asgi_application()


async def application(scope, receive, send):
    path = scope["path"]

    if path.startswith("/api"):
        _app = app
    else:
        _app = get_asgi_application()

    return await _app(scope, receive, send)
