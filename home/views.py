from django.shortcuts import render, redirect
from .models import *
from .forms import * 
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def vista_about(request):
	return render(request, 'about.html')

def vista_contacto(request):
	info_enviado=False
	email = ""
	tittle = ""
	text = ""
	if request.method == "POST":
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			info_enviado=True
			email = formulario.cleaned_data['corrreo']
			tittle = formulario.cleaned_data['titulo']
			text = formulario.cleaned_data['texto']
	else:
		formulario = contacto_form()
	return render(request, 'contacto.html',locals())

#VISTAS DE LA TABLA INSTRUMENTO

def vista_lista_instrumento(request):
	lista = Instrumento.objects.filter()
	return render(request, 'lista_instrumento.html', locals())


def vista_agregar_instrumento(request):
	if request.method == 'POST':
		formulario = agregar_instrumento_form(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return redirect ('/lista_instrumento/')
	else:
		formulario = agregar_instrumento_form()
	return render(request, 'vista_agregar_instrumento.html', locals())


def vista_ver_instrumento(request, id_ins):
	i = Instrumento.objects.get(id=id_ins)
	return render(request, 'ver_instrumento.html', locals())


def vista_editar_instrumento(request, id_ins):
	ins=Instrumento.objects.get(id = id_ins)
	if request.method == "POST":
		formulario = agregar_instrumento_form(request.POST, request.FILES, instance=ins)
		if formulario.is_valid():
			ins = formulario.save()
			return redirect('/lista_instrumento/')
	else:
		#SELECT * from home_producto WHERE id == id_ins;
		formulario=agregar_instrumento_form(instance = ins)
	return render(request, 'vista_agregar_instrumento.html', locals())

def vista_eliminar_instrumento(request, id_ins):
	ins = Instrumento.objects.get(id = id_ins)
	ins.delete()
	return redirect ('/lista_instrumento/')

#VISTAS DE LA TABLA PROVEEDOR

def vista_lista_proveedor(request):
	lista = Proveedor.objects.filter()
	return render(request, 'lista_proveedor.html', locals())
	
def vista_editar_proveedor(request, id_ins):
	ins=Proveedor.objects.get(id = id_ins)
	if request.method == "POST":
		formulario = agregar_proveedor_form(request.POST, request.FILES, instance=ins)
		if formulario.is_valid():
			ins = formulario.save()
			return redirect('/lista_proveedor/')
	else:
		#SELECT * from home_producto WHERE id == id_ins;
		formulario=agregar_proveedor_form(instance = ins)
	return render(request, 'vista_agregar_proveedor.html', locals())

def vista_agregar_proveedor(request):
	if request.method == 'POST':
		formulario = agregar_proveedor_form(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect ('/lista_proveedor/')
	else:
		formulario = agregar_proveedor_form()
	return render(request, 'vista_agregar_proveedor.html', locals())
	
def vista_ver_proveedor(request, id_ins):
	i = Proveedor.objects.get(id=id_ins)
	return render(request, 'ver_proveedor.html', locals())

def vista_eliminar_proveedor(request, id_ins):
	ins = Proveedor.objects.get(id = id_ins)
	ins.delete()
	return redirect ('/lista_proveedor/')

#VISTAS DE LA TABLA MARCA

def vista_lista_marca(request):
	lista = Marca.objects.filter()
	return render(request, 'lista_marca.html', locals())
	
def vista_editar_marca(request, id_ins):
	ins=Marca.objects.get(id = id_ins)
	if request.method == "POST":
		formulario = agregar_marca_form(request.POST, request.FILES, instance=ins)
		if formulario.is_valid():
			ins = formulario.save()
			return redirect('/lista_marca/')
	else:
		#SELECT * from home_producto WHERE id == id_ins;
		formulario=agregar_marca_form(instance = ins)
	return render(request, 'vista_agregar_marca.html', locals())

def vista_agregar_marca(request):
	if request.method == 'POST':
		formulario = agregar_marca_form(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect ('/lista_marca/')
	else:
		formulario = agregar_marca_form()
	return render(request, 'vista_agregar_marca.html', locals())
	
def vista_ver_marca(request, id_ins):
	i = Marca.objects.get(id=id_ins)
	return render(request, 'ver_marca.html', locals())

def vista_eliminar_marca(request, id_ins):
	ins = Marca.objects.get(id = id_ins)
	ins.delete()
	return redirect ('/lista_marca/')

#VISTAS DE LA TABLA VENDEDOR

def vista_lista_vendedor(request):
	lista = Vendedor.objects.filter()
	return render(request, 'lista_vendedor.html', locals())
	
def vista_editar_vendedor(request, id_ins):
	ins=Vendedor.objects.get(id = id_ins)
	if request.method == "POST":
		formulario = agregar_vendedor_form(request.POST, request.FILES, instance=ins)
		if formulario.is_valid():
			ins = formulario.save()
			return redirect('/lista_vendedor/')
	else:
		#SELECT * from home_producto WHERE id == id_ins;
		formulario=agregar_vendedor_form(instance = ins)
	return render(request, 'vista_agregar_vendedor.html', locals())

def vista_agregar_vendedor(request):
	if request.method == 'POST':
		formulario = agregar_vendedor_form(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect ('/lista_vendedor/')
	else:
		formulario = agregar_vendedor_form()
	return render(request, 'vista_agregar_vendedor.html', locals())
	
def vista_ver_vendedor(request, id_ins):
	i = Vendedor.objects.get(id=id_ins)
	return render(request, 'ver_vendedor.html', locals())

def vista_eliminar_vendedor(request, id_ins):
	ins = Vendedor.objects.get(id = id_ins)
	ins.delete()
	return redirect ('/lista_vendedor/')

#VISTAS DE LA TABLA CLIENTE

def vista_lista_cliente(request):
	lista = Cliente.objects.filter()
	return render(request, 'lista_cliente.html', locals())
	
def vista_editar_cliente(request, id_ins):
	ins=Cliente.objects.get(id = id_ins)
	if request.method == "POST":
		formulario = agregar_cliente_form(request.POST, request.FILES, instance=ins)
		if formulario.is_valid():
			ins = formulario.save()
			return redirect('/lista_cliente/')
	else:
		#SELECT * from home_producto WHERE id == id_ins;
		formulario=agregar_cliente_form(instance = ins)
	return render(request, 'vista_agregar_cliente.html', locals())

def vista_agregar_cliente(request):
	if request.method == 'POST':
		formulario = agregar_cliente_form(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect ('/lista_cliente/')
	else:
		formulario = agregar_cliente_form()
	return render(request, 'vista_agregar_cliente.html', locals())
	
def vista_ver_cliente(request, id_ins):
	i = Cliente.objects.get(id=id_ins)
	return render(request, 'ver_cliente.html', locals())

def vista_eliminar_cliente(request, id_ins):
	ins = Cliente.objects.get(id = id_ins)
	ins.delete()
	return redirect ('/lista_cliente/')

#VISTAS DE LA TABLA FACTURA

def vista_lista_factura(request):
	lista = Factura.objects.filter()
	return render(request, 'lista_factura.html', locals())
	
def vista_editar_factura(request, id_ins):
	ins=Factura.objects.get(id = id_ins)
	if request.method == "POST":
		formulario = agregar_factura_form(request.POST, request.FILES, instance=ins)
		if formulario.is_valid():
			ins = formulario.save()
			return redirect('/lista_factura/')
	else:
		#SELECT * from home_producto WHERE id == id_ins;
		formulario=agregar_factura_form(instance = ins)
	return render(request, 'vista_agregar_factura.html', locals())

def vista_agregar_factura(request):
	if request.method == 'POST':
		formulario = agregar_factura_form(request.POST)
		if formulario.is_valid():
			formulario.save()
			return redirect ('/lista_factura/')
	else:
		formulario = agregar_factura_form()
	return render(request, 'vista_agregar_factura.html', locals())
	
def vista_ver_factura(request, id_ins):
	i = Factura.objects.get(id=id_ins)
	return render(request, 'ver_factura.html', locals())

def vista_eliminar_factura(request, id_ins):
	ins = Factura.objects.get(id = id_ins)
	ins.delete()
	return redirect ('/lista_factura/')

def vista_login(request):
	usu=""
	cla=""

	if request.method == "POST":
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj = "USUARIO O CLAVE INCORRECTOS"
	formulario = login_form()
	return render(request, 'login.html',locals())

def vista_logout(request):
	logout(request)
	return redirect('/')

def vista_register(request):
	formulario = register_form()
	if request.method == 'POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usuario = formulario.cleaned_data['username']
			correo 	= formulario.cleaned_data['email']
			password_1 = formulario.cleaned_data['password_1']
			password_2 = formulario.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return render(request, 'gracias.html', locals())
		else:
			return render(request, 'register.html', locals())
	return render(request, 'register.html', locals())

def vista_perfil(request):
	form_1 = register_form()
	form_2 = perfil_form()
	if request.method == 'POST':
		form_1 = register_form(request.POST)
		form_2 = perfil_form(request.POST, request.FILES)
		if form_1.is_valid() and form_2.is_valid():
			usuario = form_1.cleaned_data['username']
			correo 	= form_1.cleaned_data['email']
			password_1 = form_1.cleaned_data['password_1']
			password_2 = form_1.cleaned_data['password_2']
			u = User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()

			z = form_2.save(commit=False)
			z.user = u
			z.save()
	return render(request, 'perfil.html', locals())

def vista_contacto(request):
	formulario = contacto_form()
	return render(request, 'contacto.html', locals())