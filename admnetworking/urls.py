"""admnetworking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls, name='house'),
    path('', views.home_view, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('registration/', views.registration, name='Registrar'),
    path('dashboard', views.HomeSystem, name='Dashboard'),
    path('guia-4to6/', views.Ipv4Ipv6intro, name='guia'),
    path('guia-4to6/pasos/', views.Ipv4Ipv6pasos, name='pasos'),
    path('guia-4to6/segmentacion/', views.SegmentacionCalculadoraipv6, name='segmento6'),
    path('calculadora-segmento/',views.SegmentacionCalculadora, name='segmento'),
    path('solicitud-usuario/', views.Solicitudcrear, name='crear solicitud'),
    path('solicitud-usuario/<int:pk>', views.Solicitudver, name='solicitudes de usuarios'),
    path('dispositivo/', views.InventarioListaDevice, name='Inventario'),
    path('dispositivo/crear', views.InventarioCrear, name='crear dispositivo'),
    path('dispositivo/<int:pk>/', views.InventarioUpdates, name='editar dispositivo'),
    path('ip/', views.IPListaReverse, name='ip'),
    path('ip/crear', views.IPCrear, name='crear ip'),
    path('ip/<int:pk>/', views.IPUpdates, name='editar ip'),
    path('ubicacion/', views.UbicacionLista, name='Lista Ubicacion'),
    path('ubicacion/crear', views.UbicacionCrear, name='Crear Ubicacion'),
    path('ubicacion/<int:pk>/', views.UbicacionUpdate, name='Editar Ubicacion'),
    path('ubicacion/<int:pk>/b', views.UbicacionBorrar, name='Borrar Ubicacion'),
    path('sendconf/', views.SendConfiguration, name='sendconf'),
    path('solicitud-usuario-f/<int:pk>/', views.Solicitudf, name='Solicitud Cambio'),
    path('inventario/<int:pk>/b', views.InventarioBorrar, name='Borrar Dispositivo'),
    path('ip/<int:pk>/b', views.IPBorrar, name='Borrar Ip'),

]
