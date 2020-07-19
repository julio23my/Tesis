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
admin.site.register(Segmento)
admin.site.register(Ubicacion)
admin.site.register(Solicitudes)
admin.site.register(IpReservada)
admin.site.register(SendConf)