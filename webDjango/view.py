from django.http import HttpResponse
from django.template import loader

def home(self, name):
    return HttpResponse(f"Hola soy {name}")

def inicio(request):
    return HttpResponse("Página principal")
