from django.urls import path
from csk.views import *
app_name='anything'
urlpatterns=[
    path('msdhoni/',msdhoni,name='madhoni'),
    path('captain/',captain,name='captain')
]