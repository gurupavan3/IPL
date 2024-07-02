from django.urls import path
from srh.views import *
app_name='something'
urlpatterns=[
    path('cummins/',cummins,name='cummins')
]