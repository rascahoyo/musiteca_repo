from django import forms
from .models import *
from django.contrib.auth.models import User



class agregar_instrumento_form(forms.ModelForm):
	class Meta:
			model = Instrumento
			fields = '__all__'
			widgets={
			'nombre':forms.TextInput(attrs = {"class":"form-control"}),
			'descripcion':forms.TextInput(attrs = {"class":"form-control"}),
			'precio':forms.NumberInput(attrs = {"class":"form-control"}),
			'marca':forms.Select(attrs = {"class":"form-control"}),
			'foto':forms.FileInput(attrs = {"class":"form-control-file "}),
			}

class agregar_cliente_form(forms.ModelForm):
	class Meta:
			model = Cliente
			fields = '__all__'
			widgets={
			'nombre':forms.TextInput(attrs = {"class":"form-control"}),
			'apellido':forms.TextInput(attrs = {"class":"form-control"}),
			'identificacion':forms.TextInput(attrs = {"class":"form-control"}),
			'direccion':forms.TextInput(attrs = {"class":"form-control "}),
			}

class agregar_proveedor_form(forms.ModelForm):
	class Meta:
			model = Proveedor
			fields = '__all__'
			widgets={
			'nombre':forms.TextInput(attrs = {"class":"form-control"}),
			'nit':forms.TextInput(attrs = {"class":"form-control"}),
			'telefono':forms.TextInput(attrs = {"class":"form-control"}),
			}


class agregar_marca_form(forms.ModelForm):
	class Meta:
			model = Marca
			fields = '__all__'
			widgets={
			'nombre':forms.TextInput(attrs = {"class":"form-control"}),
			'origen':forms.TextInput(attrs = {"class":"form-control"}),
			'garantia':forms.TextInput(attrs = {"class":"form-control"}),
			'proveedor':forms.Select(attrs = {"class":"form-control "}),
			}

class agregar_factura_form(forms.ModelForm):
	class Meta:
			model = Factura
			fields = '__all__'
			widgets={
			'precio':forms.TextInput(attrs = {"class":"form-control"}),
			'total':forms.TextInput(attrs = {"class":"form-control"}),
			'fecha':forms.TextInput(attrs = {"class":"form-control"}),
			'instrumento':forms.Select(attrs = {"class":"form-control "}),
			'vendedor':forms.Select(attrs = {"class":"form-control "}),
			'cliente':forms.Select(attrs = {"class":"form-control "}),
			}

class agregar_vendedor_form(forms.ModelForm):
	class Meta:
			model = Vendedor
			fields = '__all__'
			widgets={
			'nombre':forms.TextInput(attrs = {"class":"form-control"}),
			'apellido':forms.TextInput(attrs = {"class":"form-control"}),
			'identificacion':forms.TextInput(attrs = {"class":"form-control"}),
			}

class login_form(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput(attrs = {"class":"form-control"}))
	clave = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs = {"class":"form-control"}))

class register_form(forms.Form):
	username	=forms.CharField(widget=forms.TextInput(attrs = {"class":"form-control"}))
	email		=forms.EmailField(widget=forms.TextInput(attrs = {"class":"form-control"}))
	password_1	=forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False, attrs = {"class":"form-control"}))
	password_2	=forms.CharField(label='Confirmar Password', widget=forms.PasswordInput(render_value=False, attrs = {"class":"form-control"}))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya registrado')

	def clean_mail(self):
		email = self.cleaned_data['email']
		try:
			email = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Correo electronico ya existe')

	def clean_password(self):
		password_1 = self.cleaned_data['password_1']
		password_2 = self.cleaned_data['password_2']
		
		if password_1 == password_2:
			pass
		else:
			raise forms.ValidationError('No coinciden los password')

class perfil_form(forms.ModelForm):
		class Meta:
			model = Perfil
			fields= ['foto','nombre','identificacion','edad']
			exclude = ['user']
			widgets={
			'foto':forms.FileInput(attrs = {"class":"form-control-file "}),
			'nombre':forms.TextInput(attrs = {"class":"form-control"}),
			'identificacion':forms.TextInput(attrs = {"class":"form-control"}),
			'edad':forms.TextInput(attrs = {"class":"form-control"}),
			}

class contacto_form(forms.Form):

	nombre = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control"}))
	correo = forms.EmailField(widget = forms.TextInput(attrs = {"class":"form-control"}))
	telefono = forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control"}))
	mensaje = forms.CharField(widget = forms.Textarea(attrs = {"class":"form-control"}))
	
		