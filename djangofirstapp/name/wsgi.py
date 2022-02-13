"""
WSGI config for name project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'name.settings')

application = get_wsgi_application()




   #import os
   #import sys
#DataFlair
   #path = '/home/karansmittal/DataFlairDjango/dfdjangotutorial'
   #if path not in sys.path:
    #sys.path.append(path)
#os.chdir(path)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'dfdjangotutorial.settings'
#import django
#django.setup()
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

#put this code on case of production ur site on live remove all normal code in this file replace with these