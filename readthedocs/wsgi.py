import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'readthedocs.settings.sqlite'
application = get_wsgi_application()
