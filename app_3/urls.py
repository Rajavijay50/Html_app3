from django.urls import path
from app_3.views import *
app_name='app_3'
urlpatterns=[
    path('string/',string,name='string'),
    path('page1/',page1,name='page1'),
    path('page2/',page2,name='page2'),
]