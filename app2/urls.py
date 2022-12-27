from django.urls import path
from app2.views import *
app_name='something 1'
urlpatterns=[
    path('fourth/',fourth,name='fourth'),
     ]  