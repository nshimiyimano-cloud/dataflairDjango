from django.urls import path
from .views import *
from name import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', create_profile, name = 'create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
