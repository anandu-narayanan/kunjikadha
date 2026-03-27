"""
WSGI config for malayalam_story_creator project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'malayalam_story_creator.settings')

application = get_wsgi_application()
