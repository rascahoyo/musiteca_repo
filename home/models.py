from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	identificacion = models.CharField(max_length = 100)
	direccion = models.CharField(max_length = 100)

	def __str__(self):
		return self.nombre

class Proveedor(models.Model):
	nombre = models.CharField(max_length = 100)
	nit = models.CharField(max_length = 15)

	def __str__(self):
		return self.nombre

class Marca(models.Model):
	nombre = models.CharField(max_length = 100)
	origen = models.CharField(max_length = 100)
	garantia = models.CharField(max_length = 100)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre

class Instrumento(models.Model):
	nombre = models.CharField(max_length = 100)
	descripcion = models.TextField(max_length = 500)
	precio = models.DecimalField(max_digits = 10, decimal_places =2)		
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='instrumentos', null=True, blank=True, default="instrumentos/const.png")

	def __str__(self):
		return self.nombre

class Vendedor(models.Model):
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	identificacion = models.CharField(max_length = 100)

	def __str__(self):
		return self.nombre

class Factura(models.Model):
	precio = models.DecimalField(max_digits = 10, decimal_places =2)
	total = models.DecimalField(max_digits = 20, decimal_places =2)
	fecha = models.DateTimeField(auto_now_add=True)
	instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE)
	vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


	def __float__(self):
		return self.total

class Perfil(models.Model):
	foto = models.ImageField(upload_to='perfiles', null=True, blank=True)
	nombre = models.CharField(max_length = 100)
	identificacion = models.CharField(max_length = 100)
	edad = models.CharField(max_length = 2)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.nombre