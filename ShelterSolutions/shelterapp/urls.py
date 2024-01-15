from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('admin_reg',admin_reg),
    path('admin_log',admin_log),
    path('admin_index',admin_index),
    path('add_property',add_property),
    path('add_unit',add_unit),
    path('add_tenant',add_tenant),
    path('add_tenant_unit',add_tenant_unit),
    path('properties',property_view),
    path('property_single/<int:id>',property_single),
    path('tenant_single/<int:id>',tenant_single)
]