from django.urls import path
from app_1.views import *
app_name='app_1'

urlpatterns=[
    path('string/',string,name='string'),
    path('work1/',work1,name='work1.html'),
    path('work2/',work2,name='work2.html'),
]