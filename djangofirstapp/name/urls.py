"""name URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from . import custurls



from .views import index
from .views import setCookie
from .views import showCookie
from .views import create_session
from .views import access_session
from .views import delete_session



urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello",index),
    path('helloworld/', include('name.custurls')),
    path('student/',include('student.urls')),
    path('setcookie/',setCookie),
    path('getcookie/',showCookie),
    path('create-session/',create_session),
    path('get-session/',access_session),
    path('delete-session/',delete_session),
    path('subscribe/', include('subscribe.urls')),
    path('registration',include('registration.urls')),
    path('',include('home.urls')),
    path('upload/', include('profile_maker.urls')),
    path('ajax/',include('post.urls'))
]

    

