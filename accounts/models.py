from django.db import models
import uuid

# Create your models here.
class Ubicacion(models.Model):
    localidad = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50, blank=True, null=True)


class Device(models.Model):
    ROUTER = 'R'
    SWITCH = 'SW'
    FIREWALL = 'F'
    SERVIDOR = 'SR'
    ROUTERW = 'RW'
    ENDEV = 'ED'
    Type_Devices = [
        (ROUTER, 'Router'),
        (SWITCH, 'Switch'),
        (FIREWALL, 'Firewall'),
        (SERVIDOR, 'Servidor'),
        (ROUTERW, 'Router WIFI'),
        (ENDEV, 'End Device'),

    ]
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    dvt =  models.CharField(max_length=2,choices=Type_Devices,default=SWITCH, verbose_name='Tipo de Dispositivos')
    ipv4 = models.GenericIPAddressField(protocol='IPv4', verbose_name='IPv4 De Acceso', blank=True, null=True)
    ipv6 = models.GenericIPAddressField(protocol='IPv6',verbose_name='IPv6 De Acceso', blank=True, null=True)
    ssh = models.BooleanField(blank=True, null=True)
    telnet = models.BooleanField(blank=True, null=True)
    conf = models.FileField(blank=True, null=True)
    conf_t = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name='Hostname',blank=True, null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Ubicacion del Equipo')

class Puerto(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Puerto del Dispositivo')
    puerto = models.CharField(max_length=50,blank=True, null=True)
    vlan = models.IntegerField(default=1,blank=True, null=True)
    mac = models.CharField(max_length=50,blank=True, null=True)
    ipv4 = models.GenericIPAddressField(protocol='IPv4', verbose_name='IPv4',blank=True, null=True)
    ipv6 = models.GenericIPAddressField(protocol='IPv6',verbose_name='IPv6',blank=True, null=True)
    actv = models.BooleanField(default=False)


