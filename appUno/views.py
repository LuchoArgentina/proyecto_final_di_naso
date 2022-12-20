from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "appUno/index.html")

def jugadores(request):
    return render(request, "appUno/jugadores.html")

def partidos(request):
    return render(request, "appUno/partidos.html")

def goles(request):
    return render(request, "appUno/goles.html")
