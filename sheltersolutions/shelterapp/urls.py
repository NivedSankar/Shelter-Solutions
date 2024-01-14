from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('admin_reg',admin_reg),
    path('admin_log',admin_log),
    path('admin_index',admin_index),
    path('add_property',add_property)
]