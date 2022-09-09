from django.http import HttpResponse
from django.template import loader

def home(self, name):
    return HttpResponse(f"Hola soy {name}")

def inicio(request):
    return HttpResponse("Página principal")

def homePage(self):
    lista = [1,2,3,4,5]
    data = {"nombre": "Manuel", "apellido": "Vilela", "lista" : lista}
    planilla = loader.get_template("home.html")
    documento = planilla.render(data)
    return HttpResponse(documento)
