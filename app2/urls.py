from django.urls import path
from app2.views import *
app_name='naveen'

urlpatterns=[
    path('navi/',navi,name='navi')
]