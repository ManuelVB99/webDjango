from django.urls import path
from AppCoder.view import *

urlpatterns = [
    path('', inicio),
    path("cursos/", cursos),
    path("profesores/", profesores),
    path("entregables/", entregables),
    path("estudiantes/", estudiantes)
]