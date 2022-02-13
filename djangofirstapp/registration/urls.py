from django.urls import path

from .views import regform

urlpatterns = [
    path('',regform,name='registrationform')
]
