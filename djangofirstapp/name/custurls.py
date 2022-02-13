from django.urls import path
#from .views import index
from .views import htmlpage

urlpatterns=[
    path('',htmlpage,name='helloworldpage')  #this way trully enhance codes readability instead use cache_page(200) as decorator before function this funct take 1 argument of expiration
]
