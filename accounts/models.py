from django.db import models
from netaddr import *
import uuid
import pprint

# Inventario View
class Ubicacion(models.Model):
    localidad = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50, blank=True, null=True)

# Inventario, SendConf View
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

# Inventario,SendConf View
class Puerto(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Puerto del Dispositivo')
    puerto = models.CharField(max_length=50,blank=True, null=True)
    vlan = models.IntegerField(default=1,blank=True, null=True)
    mac = models.CharField(max_length=50,blank=True, null=True)
    ipv4 = models.GenericIPAddressField(protocol='IPv4', verbose_name='IPv4',blank=True, null=True)
    ipv6 = models.GenericIPAddressField(protocol='IPv6',verbose_name='IPv6',blank=True, null=True)
    actv = models.BooleanField(default=False)


#Logs
class Log(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Logs del Dispositivo')
    log = models.CharField(max_length=2500, blank=True, null=True)
    alerta = models.BooleanField()

#Usuarios
class Usuario(models.Model):
    name = models.CharField(max_length=10)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Usuario del Dispositivo')
    ssh = models.BooleanField(blank=True, null=True)
    telnet = models.BooleanField(blank=True, null=True)
    activo = models.BooleanField()


#IPV4 to IPV6 View
class Segmento(models.Model):
    #Rango de direcciones ip 190.170.128.0/18
    rango = models.CharField(max_length=50,blank=True, null=True)
    # Mascara de subred
    mascara = models.CharField(max_length=50,blank=True, null=True)
    # Cantidad de direcciones IP
    direccion = models.IntegerField(verbose_name='Numero de usuarios', blank=True, null=True)
    # Segmentaciones de rangos IP 190.170.129.129/25 cantidades
    subredes = models.IntegerField(verbose_name='Numero de subredes')
    # Reservadas IP
    reserv = models.IntegerField(blank=True, null=True)



