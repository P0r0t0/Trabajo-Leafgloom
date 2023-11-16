from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render 
import requests

# import requests

url = "https://perenual.com/api/species-list?key=sk-24d46532eef6848082612"
response = requests.get(url)
if response.status_code == 200:
    datos = response.json()
else:
    datos = {"error":[]}


def Pagina_inicial(request):

   ##doc_externo = open("C:/Users/kz17a/OneDrive/Escritorio/Proyectos de intro/Leafgloom/leafgloom/plantillas/Logo.html")
   ##plt = Template(doc_externo.read())
   ##doc_externo.close()

   #doc_externo = loader.get_template("Logo.html") 
   ##ctx = Context()
   #documento = doc_externo.render()
   
   return render(request, "Logo.html") #se puede poner un tercer parametro que seria el contexto, este caso no trae


# Se esta intentando que aparezca informacion de la planata selecionadad en listado por cada catalogo
def catalogo(request,nombre_planta):

    doc_externo = loader.get_template("Catalogo.html")

    documento = doc_externo.render({"other_name": nombre_planta })

    return HttpResponse(documento)



def listado(request):

    return render(request, "listado.html",datos)

def plantas(request):
    return render(request, "plantas.html")

def home(request):
    return render(request, "home.html")