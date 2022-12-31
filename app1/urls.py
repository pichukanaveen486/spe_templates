from django.urls import path
from app1.views import *
app_name='jaanuu'

urlpatterns=[
    path('jaanu/',jaanu,name='jaanu')
]