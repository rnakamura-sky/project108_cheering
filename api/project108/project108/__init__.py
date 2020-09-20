# This will make sure the app is always imported when
# Django starts so that shared task will use this app.
from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

__all__ = ('celery_app',)
