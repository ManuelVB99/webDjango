from django.urls import path
from AppCoder.view import *

urlpatterns = [
    path('', inicio),
    path("cursos/", cursos),
    path("profesores/", profesores),
    path("entregables/", entregables),
    path("estudiantes/", estudiantes),
    path("home/", home),
    path("api_estudiantes/", api_estudiantes),
    path("buscar_estudiante/", buscar_estudiante)
]