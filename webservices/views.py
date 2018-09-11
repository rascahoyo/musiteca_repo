from django.shortcuts import render
from home.models import *
from .serializer import *
from rest_framework import viewsets
# Create your views here.

class instrumento_viewset(viewsets.ModelViewSet):
	queryset = Instrumento.objects.all()
	serializer_class = instrumento_serializer

class marca_viewset(viewsets.ModelViewSet):
	queryset = Marca.objects.all()
	serializer_class = marca_serializer

class proveedor_viewset(viewsets.ModelViewSet):
	queryset = Proveedor.objects.all()
	serializer_class = proveedor_serializer

class vendedor_viewset(viewsets.ModelViewSet):
	queryset = Vendedor.objects.all()
	serializer_class = vendedor_serializer

class factura_viewset(viewsets.ModelViewSet):
	queryset = Factura.objects.all()
	serializer_class = factura_serializer

class cliente_viewset(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = cliente_serializer
