from rest_framework import serializers
from home.models import *

class instrumento_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Instrumento
		fields = ('url','nombre','descripcion','marca','foto',)

class marca_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Marca
		fields = ('url','nombre','origen','garantia','proveedor',)

class proveedor_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Proveedor
		fields = ('url','nombre','nit',)

class vendedor_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Vendedor
		fields = ('url','nombre','apellido','identificacion',)

class factura_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Factura
		fields = ('url','precio','total','fecha','instrumento','vendedor','cliente',)

class cliente_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cliente
		fields = ('url','nombre','apellido','identificacion','direccion',)
