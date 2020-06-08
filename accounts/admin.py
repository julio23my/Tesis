from django.contrib import admin
from .models import *
# Register your models here.

class PuertoInline(admin.TabularInline):
    model = Puerto

class DeviceAdmin(admin.ModelAdmin):
    inlines = [
        PuertoInline,
    ]
admin.site.register(Device, DeviceAdmin)