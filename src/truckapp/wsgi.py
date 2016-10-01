"""
WSGI config for truckapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys
# add the hellodjango project path into the sys.path
path = '/Users/jongaither/truckapp/src/truckapp/settings'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# add the virtualenv site-packages path to the sys.path
sys.path.append('/Users/jongaither/truckapp/myvenv/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "truckapp.settings")

application = get_wsgi_application()
