from django.db import models
import uuid

# Create your models here.
class Ubicacion(models.Model):
    localidad = models.CharField(max_length=255)


class Device(models.Model):
    ROUTER = 'R'
    SWITCH = 'SW'
    FIREWALL = 'F'
    SERVIDOR = 'SR'
    ROUTERW = 'RW'
    Type_Devices = [
        (ROUTER, 'Router'),
        (SWITCH, 'Switch'),
        (FIREWALL, 'Firewall'),
        (SERVIDOR, 'Servidor'),
        (ROUTERW, 'Router WIFI'),
    ]
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    dvt =  models.CharField(max_length=2,choices=Type_Devices,default=SWITCH, verbose_name='Tipo de Dispositivos')
    ipv4 = models.GenericIPAddressField(protocol='IPv4', verbose_name='IPv4 De Acceso')
    ipv6 = models.GenericIPAddressField(protocol='IPv6',verbose_name='IPv6 De Acceso')
    ssh = models.BooleanField()
    telnet = models.BooleanField()
    conf = models.FileField()
    conf_t = models.TextField()

class Puerto(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True)
    puerto = models.CharField(max_length=50,blank=True, null=True)
    vlan = models.IntegerField(default=1,blank=True, null=True)
    mac = models.CharField(max_length=50,blank=True, null=True)
    ipv4 = models.GenericIPAddressField(protocol='IPv4', verbose_name='IPv4',blank=True, null=True)
    ipv6 = models.GenericIPAddressField(protocol='IPv6',verbose_name='IPv6',blank=True, null=True)

