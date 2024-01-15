from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(property)
admin.site.register(Unit)
admin.site.register(tenant)
admin.site.register(tenant_unit)