from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario, Vehiculo,Reserva_Inicial1
from reservas.forms import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes




# Create your views here.


def login(request):
    return render(request, 'login.html')

def login_error(request):
    return render(request, 'login_error.html')

def home_admin(request):
    return render(request, 'home_admin.html')

def crud_agenda_inicial1(request):
    context={}
    return render(request, 'crud_agenda_inicial1.html',context)

def crud_agenda_inicial1_editar(request):
    return render(request, 'crud_agenda_inicial1_editar.html')

def crud_agenda_inicial1_listar(request):
    reservas_iniciales1=Reserva_Inicial1.objects.all()
    return render (request, 'crud_agenda_inicial1_listar.html',{"reserva_inicial1":reservas_iniciales1})
      
def crud_agenda_inicial2(request):
    return render(request, 'crud_agenda_inicial2.html')

def crud_agenda_final1(request):
    return render(request, 'crud_agenda_final1.html')

def crud_agenda_final2(request):
    return render(request, 'crud_agenda_final2.html')

def crud_usuarios(request):
    return render(request, 'crud_usuarios.html')

def crud_vehiculos(request):
    return render(request, 'crud_vehiculos.html')

def crud_vehiculos_editar(request):
    return render(request, 'crud_vehiculos_editar.html')

def vehiculos_add(request):
    print ("estoy en controlador vehiculos_add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            id_vehiculo = request.POST.get("id_vehiculo")
            patente = request.POST["patente"]
            marca = request.POST["marca"] 
            modelo = request.POST["modelo"]
            anio = request.POST["anio"]
           
            
            
            if id_vehiculo != "":
                
                vehiculo = Vehiculo()
                
                vehiculo.id_vehiculo = id_vehiculo
                vehiculo.patente = patente
                vehiculo.marca = marca
                vehiculo.modelo = modelo
                vehiculo.anio = anio
                
                
                vehiculo.save()
                
                context={"mensaje":"Vehiculo agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
              
        
    return render (request, 'crud_vehiculos.html', context)


def vehiculos_del (request, pk):  
    vehiculo = Vehiculo.objects.get(id_vehiculo=pk)
    context={}
    if vehiculo:
        vehiculo.delete()
        return redirect(to='crud_vehiculos_listar')
    
def vehiculos_edit (request, pk):

    vehiculo = Vehiculo.objects.get(id_vehiculo=pk)

    datos = {
        'form': VehiculoForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario2 = VehiculoForm(data=request.POST, instance=vehiculo)
        if formulario2.is_valid:
            formulario2.save(),
            datos['mensaje'] = "Los cambios han sido modificados correctamente"  
    return render(request, 'crud_vehiculos_editar.html', datos)

def crud_vehiculos_listar(request):
    vehiculos=Vehiculo.objects.all()
    data = {'vehiculo':vehiculos}
    return render (request, 'crud_vehiculos_listar.html',data)


def home_user(request):
    return render(request, 'home_user.html')

def mi_perfil(request):
    return render(request, 'mi_perfil.html')

def mi_perfil_editar_datos(request):
    return render(request, 'mi_perfil_editar_datos.html')

def mi_perfil_historial_solicitudes(request):
    return render(request, 'mi_perfil_historial_solicitudes.html')

def listado_conductores(request):
    return render(request, 'listado_conductores.html')

def listado_reservas1(request):
    return render(request, 'listado_reservas1.html')

def listado_reservas1_solicitudes_anteriores(request):
    return render(request, 'listado_reservas1_solicitudes_anteriores.html')

def listado_reservas2(request):
    return render(request, 'listado_reservas2.html')

def listado_reservas2_solicitudes_anteriores(request):
    return render(request, 'listado_reservas2_solicitudes_anteriores.html')

def formulario_agenda_inicial1(request):
    return render(request, 'formulario_agenda_inicial1.html')

def formulario_agenda_inicial2(request):
    return render(request, 'formulario_agenda_inicial2.html')

def formulario_agenda_final1(request):
    return render(request, 'formulario_agenda_final1.html')

def formulario_agenda_final2(request):
    return render(request, 'formulario_agenda_final2.html')

def cerrar_sesion(request):
    return render(request, 'cerrar_sesion.html')

def usuariosAdd(request):
    print ("estoy en controlador usuariosAdd... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")

        if opcion=="Agregar":
            
            rut = request.POST["rut"]
            nombre = request.POST["nombre"]
            apellido_paterno = request.POST["apellido_paterno"]
            apellido_materno = request.POST["apellido_materno"]
            fecha_nacimiento = request.POST["fecha_nacimiento"]
            genero = request.POST["genero"]
            
            
            if rut != "" and nombre != "":
                
                usuario = Usuario()
                
                usuario.rut = rut
                usuario.nombre = nombre
                usuario.apellido_paterno = apellido_paterno
                usuario.apellido_materno = apellido_materno
                usuario.fecha_nacimiento = fecha_nacimiento
                usuario.genero = genero
                
                usuario.save()
                context["mensaje"] = "Guardado correctamente"
            else:
                context["mensaje"] = "Error"
        
    return render (request, 'tdguitarras/adminusuarios.html', context)

def reserva_inicial1_Add(request):
    print ("estoy en controlador reserva_inicial1Add... ")
    context = {}
    if request.method == "POST":
        print ("controlador es un POST... ")
        opcion = request.POST.get("opcion","")
        
        print(request.FILES)
       
    
        if True:
            
            motivo1 = request.POST["motivo1"]
            direccion1 = request.POST["direccion1"]
            foto_tacometro1 = request.FILES.get("foto_tacometro1")
            
            if id != "" and motivo1 != "": 
                
                reserva_inicial1 = Reserva_Inicial1()
                
                
                
                reserva_inicial1.motivo1 = motivo1
                reserva_inicial1.direccion1 = direccion1
                reserva_inicial1.foto_tacometro1 = foto_tacometro1
                
                reserva_inicial1.save()
                
                context={"mensaje":"reserva inicial 1 agregado correctamente"}
            else:
                context={"mensaje": "Error, los campos no pueden estar vacios"}
        else:
            context={"mensaje": "Error, los campos no pueden estar vacios"}
            return render (request, 'home_admin.html', context)         
        
    return render (request, 'home_admin.html', context)

def reserva_inicial1_Del(request,pk):
    reserva_inicial1 = Reserva_Inicial1.objects.get(id=pk)
    context={}
    if reserva_inicial1:
        reserva_inicial1.delete()
        return redirect(to='crud_agenda_inicial1_listar')
    
def reserva_inicial1_Edit (request, pk):

    reserva_inicial1 = Reserva_Inicial1.objects.get(id=pk)

    datos = {
        'form': Reserva_Inicial1Form(instance=reserva_inicial1)
    }

    if request.method == 'POST':
        formulario1 = Reserva_Inicial1Form(data=request.POST, instance=reserva_inicial1)
        if formulario1.is_valid:
            formulario1.save(),
            datos['mensaje'] = "Los cambios han sido modificados correctamente"  
    return render(request, 'crud_agenda_inicial1_editar.html', datos)      


    
    