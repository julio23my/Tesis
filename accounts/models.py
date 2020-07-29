from django.db import models
from netaddr import *
import uuid
import pprint

# Inventario View
class Ubicacion(models.Model):
    localidad = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50, blank=True, null=True)


#ParentModel.objects.exclude(childrenmodel_set__isnull=True)
# Inventario, SendConf View
class Device(models.Model):
    ROUTER = 'R'
    SWITCH = 'SW'
    FIREWALL = 'F'
    SERVIDOR = 'SR'
    ROUTERW = 'RW'
    ENDEV = 'ED'
    Type_Devices = [
        ('R', 'Router'),
        ('S', 'Switch'),
        ('F', 'Firewall'),
        ('SR', 'Servidor'),
        ('RW', 'Router WIFI'),
        ('ED', 'End Device'),

    ]
    #id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    dvt =  models.CharField(max_length=2,choices=Type_Devices, verbose_name='Tipo de Dispositivos')
    ipv4 = models.GenericIPAddressField(protocol='IPv4', verbose_name='IPv4')
    ipv6 = models.GenericIPAddressField(protocol='IPv6',verbose_name='IPv6')
    ssh = models.BooleanField(blank=True, null=True, verbose_name='SSH')
    telnet = models.BooleanField(blank=True, null=True, verbose_name='Telnet')
    conf = models.FileField(upload_to='media/',blank=True, null=True, verbose_name='Archivo')
    conf_t = models.TextField(blank=True, null=True, verbose_name='Configuracion')
    username = models.CharField(max_length=50, verbose_name='Usuario de Acceso', blank=True, null=True)
    clave = models.CharField(max_length=50, verbose_name='Clave de Acceso', blank=True, null=True)
    name = models.CharField(max_length=50, verbose_name='Hostname',blank=True, null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Ubicacion del Equipo')
    modelo = models.CharField(max_length=50, blank=True, null=True, verbose_name='Modelo')
    serial = models.CharField(max_length=50, blank=True, null=True, verbose_name='Serial')
    marca = models.CharField(max_length=50, blank=True, null=True, verbose_name='Marca')
    responsable = models.CharField(max_length=50, blank=True, null=True, verbose_name='Responsable')

    def __str__(self):
        return '%s, %s'%(self.get_dvt_display(), self.ipv4)


# Inventario,SendConf View
class Puerto(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Dispositivo')
    puerto = models.CharField(max_length=50,blank=True, null=True, verbose_name='Puerto')
    vlan = models.IntegerField(default=1,blank=True, null=True, verbose_name='Vlan')
    mac = models.CharField(max_length=50,blank=True, null=True, verbose_name='Mac')
    ipv4 = models.GenericIPAddressField(protocol='IPv4', verbose_name='IPv4',blank=True, null=True)
    ipv6 = models.GenericIPAddressField(protocol='IPv6',verbose_name='IPv6',blank=True, null=True)
    actv = models.BooleanField(default=False, verbose_name='Puerto Activo')


#Logs
class Log(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True,verbose_name='Dispositivo')
    log = models.CharField(max_length=2500, blank=True, null=True, verbose_name='Log')
    alerta = models.BooleanField(verbose_name='Alerta')




#IPV4 to IPV6 View
class Segmento(models.Model):
    MASK = [
        ('8','255.0.0.0/8'),
        ('9', '255.128.0.0/9'),
        ('10', '255.192.0.0/10'),
        ('11', '255.224.0.0/11'),
        ('12', '255.240.0.0/12'),
        ('13', '255.248.0.0/13'),
        ('14', '255.252.0.0/14'),
        ('15', '255.254.0.0/15'),
        ('16', '255.255.0.0/16'),
        ('17', '255.255.128.0/17'),
        ('18', '255.255.192.0/18'),
        ('19', '255.255.224.0/19'),
        ('20', '255.255.240.0/20'),
        ('21', '255.255.248.0/21'),
        ('22', '255.255.252.0/22'),
        ('23', '255.255.254.0/23'),
        ('24', '255.255.255.0/24'),
        ('25', '255.255.255.128/25'),
        ('26', '255.255.255.192/26'),
        ('27', '255.255.255.224/27'),
        ('28', '255.255.255.240/28'),
        ('29', '255.255.255.248/29'),
        ('30', '255.255.255.252/30'),
        ('31', '255.255.255.254/31'),
        ('32', '255.255.255.255/32'),

    ]
    #Rango de direcciones ip 190.170.128.0/18
    rango = models.CharField(max_length=50, verbose_name='Rango IP')
    # Mascara de subred
    mascara = models.CharField(max_length=50, choices=MASK, verbose_name='Mascara')
    # Cantidad de direcciones IP
    direccion = models.IntegerField(verbose_name='Numero de usuarios', blank=True, null=True)
    # Segmentaciones de rangos IP 190.170.129.129/25 cantidades
    subredes = models.IntegerField(verbose_name='Numero de subredes', default=0, blank=True, null=True)
    # Reservadas IP
    reserv = models.IntegerField(blank=True, null=True, verbose_name='Numero de IP Reservadas')

    def save(self, *args, **kwargs):
        ip = IPNetwork(self.rango)
        subnets = list(ip.subnet(int(self.mascara)))
        super(Segmento, self).save(*args, **kwargs)

    def listadirecciones(self):
        ip = IPNetwork(self.rango)
        subnets = list(ip.subnet(int(self.mascara)))
        return list(subnets)

# Direcciones IP reservadas
class IpReservada(models.Model):
    ipv4 = models.GenericIPAddressField(protocol='IPv4', verbose_name='IPv4', blank=True, null=True)
    ipv6 = models.GenericIPAddressField(protocol='IPv6', verbose_name='IPv6', blank=True, null=True)
    mac = models.CharField(max_length=50, verbose_name='MAC')
    descripcion = models.TextField(verbose_name='Descripcion')
    dispositivo = models.ForeignKey(Device, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Dispositivo')

class Solicitudes(models.Model):
    SOL = [
        ('0', 'Falla de conexion'),
        ('1', 'Expansion de red'),
        ('2', 'Solicitud de IP reservada'),
    ]
    usuario = models.CharField(max_length=50, verbose_name='Usuario')
    solicitud = models.CharField(max_length=200, choices=SOL, verbose_name='Tipo de Solicitud')
    descripcion = models.TextField(verbose_name='Descripcion')
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Ubicacion')
    completa = models.BooleanField(default=False, verbose_name='Finalizada')
    creacion = models.DateTimeField(auto_created=True, auto_now=True)

    def solicitud_verbose(self):
        return dict(Solicitudes.SOL)[self.solicitud]



class SendConf(models.Model):
    devices = models.ManyToManyField(Device)
    conf = models.TextField(verbose_name='Configuracion a Enviar')


