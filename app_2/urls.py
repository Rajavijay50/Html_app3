from django.urls import path
from app_2.views import *
app_name='app_2'

urlpatterns=[
    path('string/',string,name='string'),
    path('home1/',home1,name='home1.html'),
    path('home2/',home2,name='home2.html'),
]