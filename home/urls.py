from django.urls import path
from .views import *
from django.contrib.auth.models import User

urlpatterns =[
	path('', vista_about),
	path('contacto/', vista_contacto),
    #URLS INSTRUMENTO
    path('lista_instrumento/',vista_lista_instrumento, name='vista_lista_instrumento'),
    path('agregar_instrumento/',vista_agregar_instrumento, name='vista_agregar_instrumento'),
    path('ver_instrumento/<int:id_ins>/',vista_ver_instrumento, name='vista_ver_instrumento'),
    path('editar_instrumento/<int:id_ins>/',vista_editar_instrumento, name='vista_agregar_instrumento'),
    path('eliminar_instrumento/<int:id_ins>/',vista_eliminar_instrumento, name='vista_eliminar_instrumento'),
    #URLS PROVEEDOR
    path('lista_proveedor/',vista_lista_proveedor, name='vista_lista_proveedor'),
    path('agregar_proveedor/',vista_agregar_proveedor, name='vista_agregar_proveedor'),
    path('ver_proveedor/<int:id_ins>/',vista_ver_proveedor, name='vista_ver_proveedor'),
    path('editar_proveedor/<int:id_ins>/',vista_editar_proveedor, name='vista_agregar_proveedor'),
    path('eliminar_proveedor/<int:id_ins>/',vista_eliminar_proveedor, name='vista_eliminar_proveedor'),
    #URLS MARCA
    path('lista_marca/',vista_lista_marca, name='vista_lista_marca'),
    path('agregar_marca/',vista_agregar_marca, name='vista_agregar_marca'),
    path('ver_marca/<int:id_ins>/',vista_ver_marca, name='vista_ver_marca'),
    path('editar_marca/<int:id_ins>/',vista_editar_marca, name='vista_agregar_marca'),
    path('eliminar_marca/<int:id_ins>/',vista_eliminar_marca, name='vista_eliminar_marca'),
    #URLS VENDEDOR
    path('lista_vendedor/',vista_lista_vendedor, name='vista_lista_vendedor'),
    path('agregar_vendedor/',vista_agregar_vendedor, name='vista_agregar_vendedor'),
    path('ver_vendedor/<int:id_ins>/',vista_ver_vendedor, name='vista_ver_vendedor'),
    path('editar_vendedor/<int:id_ins>/',vista_editar_vendedor, name='vista_agregar_vendedor'),
    path('eliminar_vendedor/<int:id_ins>/',vista_eliminar_vendedor, name='vista_eliminar_vendedor'),
    #URLS CLIENTE
    path('lista_cliente/',vista_lista_cliente, name='vista_lista_cliente'),
    path('agregar_cliente/',vista_agregar_cliente, name='vista_agregar_cliente'),
    path('ver_cliente/<int:id_ins>/',vista_ver_cliente, name='vista_ver_cliente'),
    path('editar_cliente/<int:id_ins>/',vista_editar_cliente, name='vista_agregar_cliente'),
    path('eliminar_cliente/<int:id_ins>/',vista_eliminar_cliente, name='vista_eliminar_cliente'),
    #URLS FACTURA
    path('lista_factura/',vista_lista_factura, name='vista_lista_factura'),
    path('agregar_factura/',vista_agregar_factura, name='vista_agregar_factura'),
    path('ver_factura/<int:id_ins>/',vista_ver_factura, name='vista_ver_factura'),
    path('editar_factura/<int:id_ins>/',vista_editar_factura, name='vista_agregar_factura'),
    path('eliminar_factura/<int:id_ins>/',vista_eliminar_factura, name='vista_eliminar_factura'),

    path('login/',vista_login, name='vista_login'),
    path('logout/',vista_logout, name='vista_logout'),
    path('register/',vista_register, name='vista_register'),
    path('perfil/',vista_perfil, name='vista_perfil'),
]