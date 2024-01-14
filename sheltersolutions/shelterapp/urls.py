from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('admin_reg',admin_reg)
]