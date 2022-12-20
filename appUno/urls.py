from django.urls import path
from .views import *

urlpatterns = [
    path("goles/", goles, name="goles"),         #El name sirve luego para el template.
    path("jugadores/", jugadores, name="jugadores"),
    path("partidos/", partidos, name="partidos"),
    path("", index, name="index"),
]