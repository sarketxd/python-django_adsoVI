from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from django.contrib import messages
from .forms import add_usuario
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

class persona():

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

# ///////////////////////////////////////////////FORMA 1
# def registro(request):
#     if request.method == 'POST':
#         form = formulario_registro(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             messages.success(request, f'Usuario { username } cargado exitosamente !!!') 
#         else:
#             messages.success(request, 'Usuario NO cargado !!!')
#     else:
#         form = formulario_registro()        
#     context = {'form': form}
#     return render(request,"registro.html",context)


# ///////////////////////////////////////FORMA 2 
def crear_usuario(request):
    if request.method == 'POST':
        form = add_usuario(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.nombre = form.cleaned_data['nombre']
            var.apellidos = form.cleaned_data['apellidos']
            var.password = make_password(form.cleaned_data['password'])
            var.save()  # Guardar campos a la DB
            messages.success(request, 'Usuario creado correctamente.')
            return redirect('/crear')  # Redirigir a otra vista después de guardar
        else:
            messages.error(request, 'Error al crear usuario. Revise los datos.')
    else:
        form = add_usuario()
        
    context = {'form': form}
    return render(request, 'crear_usuario.html', context)


def saludo(request):
    a=4
    b=5
    c=a+b 
    texto="""
    <span> La suma de a + b es: %s <span> 
    """%(c)
    return HttpResponse(texto)

def calcular_edad(request, ano):
    edad_actual=21
    periodo=ano-2024
    edad_futura=ano+periodo
    texto = """ 
    en el año %s, la edad calculada será %s 
    """%(ano,edad,futura)
    return HttpResponse(texto)

def msg_saludo(request):
  
    p1=persona("Juan","solano")
    temas=["POO","AJAX","PHP","PYTHON","Juan"]

    # doc_externo=get_template("index.html")
    # texto=doc_externo.render({"n_nombre":p1.nombre,"n_apellido":p1.apellido,"temas":temas })
      
    # return HttpResponse(texto)
    return render(request,"index.html",{"n_nombre":p1.nombre,"n_apellido":p1.apellido,"temas":temas })

            
            
    return HttpResponse("Bienvenido a Django ")

@login_required
def crud(request):
    return render(request,"registo.html")

def registro(request):
    return render(request, "registration/registro2.html")