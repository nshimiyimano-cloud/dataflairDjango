from django.urls import path
from . import views
from .views import student_show
#from .views import setCookie

urlpatterns=[
    path('',views.student_show,name='student_show')
]



urlpattern=[
    path('',student_show,name='studentpage'),
    #path('',setCookie)
]

#ways that u can use redirect

#from django.views.generic.base import RedirectView 
# path('djangotutor/', RedirectView.as_view(url = ‘https://data-flair.training/blogs/category/django/’)),