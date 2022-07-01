from calendar import c
from cgitb import html
from django.shortcuts import render
from app_gestion.models import Persona
from django.http import HttpResponse
from django.views.generic import TemplateView



# Create your views here.
def ingresar_persona(request):
    return render(request,"ingresar_persona.html")

def index(request):
    return render(request,"index.html")

def buscar(request):
    return render(request,"buscar.html")


def listar_persona(request):
    return render(request,"listar_persona.html")


def eliminar_rut(request):
    return render(request,"eliminar_rut.html")

# Create your views here.

def listar_todo_persona(request):
    datos = Persona.objects.all()  
    return render(request,"listar_persona.html",{'personas':datos})
    
def ingreso_persona(request):
    nombre=request.GET["txt_nombre"]
    rut=request.GET["txt_rut"]
    apPaterno=request.GET["txt_appaterno"]
    apMaterno=request.GET["txt_apmaterno"]
    edad=request.GET["txt_edad"]
    vacuna=request.GET["txt_vacuna"]
    fecha=request.GET["date_fecha"]

    if len(nombre)>0 and len(rut)>0 and len(apPaterno)>0 and len(apMaterno)>0 and len(edad)>0 and len(vacuna)>0 and len(fecha)>0:
        pro=Persona(nombre=nombre,rut=rut,apPaterno=apPaterno,apMaterno=apMaterno,edad=edad,fecha=fecha,vacuna=vacuna)  
        pro.save()
        mensaje="La persona se ha ingresado correctamente..."
    else:
        mensaje="Error. no se pudo completar la operación"
        
    return HttpResponse(mensaje)
    

def buscar_persona(request):
    if request.GET["txt_persona"]:
        persona = request.GET["txt_persona"]
        personas = Persona.objects.filter(nombre__icontains=persona)
        return render(request,"listar.html",{"personas":personas,"query":persona})
    else:
        mensaje = "Debe ingresar el nombre de la persona"
        return HttpResponse(mensaje)


def eliminacion_rut(request):
    if request.GET["txt_rut"]:
        rut_recibido = request.GET["txt_rut"]
        persona = Persona.objects.filter(rut=rut_recibido)
        if persona:
            pro=Persona.objects.get(rut=rut_recibido)
            pro.delete()
            mensaje = "La persona a sido eliminada."
        else:
            mensaje = "Error. Persona no eliminada..."
    else:
        mensaje = "Debe ingresar un RUT"
    return HttpResponse(mensaje)
