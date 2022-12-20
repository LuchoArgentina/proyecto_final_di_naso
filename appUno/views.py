from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def index(request):
    return render(request, "appUno/index.html")

def jugadores(request):
    if  request.method=="POST":
        nombre= request.POST["nombre"]
        puesto= request.POST["puesto"]
        camiseta= request.POST["camiseta"]
        jugadores= Jugadores(nombre=nombre, puesto=puesto, camiseta=camiseta)
        jugadores.save()
        return render (request, "appUno/jugadores.html", {"mensaje":"Registro guardado correctamente"})
    else:
        return render(request, "appUno/jugadores.html")

def partidos(request):
    if  request.method=="POST":
        rival= request.POST["rival"]
        instancia = request.POST["instancia"]
        resultado = request.POST["resultado"]
        partidos= Partidos(rival=rival, instancia=instancia, resultado=resultado)
        partidos.save()
        return render (request, "appUno/partidos.html", {"mensaje":"Registro guardado correctamente"})
    else:
        return render(request, "appUno/partidos.html")    

def goles(request):
    if  request.method=="POST":
        nombre= request.POST["nombre"]
        goles = request.POST["goles"]
        goles= Goles(nombre=nombre, goles=goles)
        goles.save()
        return render (request, "appUno/goles.html", {"mensaje":"Registro guardado correctamente"})
    else:
        return render(request, "appUno/goles.html")


def tecnicos(request):
    if  request.method=="POST":
        nombre= request.POST["nombre"]
        apellido = request.POST["apellido"]
        rol = request.POST["rol"]
        tecnicos= Tecnicos(nombre=nombre, apellido=apellido, rol=rol)
        tecnicos.save()
        return render (request, "appUno/tecnicos.html", {"mensaje":"Registro guardado correctamente"})
    else:
        return render(request, "appUno/tecnicos.html")
