from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render 
import requests

# import requests

##
# se movio la extraccion de datos a la parte logica del codigo
url = "https://perenual.com/api/species-list?key=sk-24d46532eef6848082612"
response = requests.get(url)
if response.status_code == 200:
    datos = response.json()
else:
    datos = {"error":[]}
##

def Pagina_inicial(request):

   return render(request, "Logo.html") #se puede poner un tercer parametro que seria el contexto, este caso no trae

##
# se esta intentando que el display de información sea lindo :P
# la info de la planta se saca llamando entre {{ }} la llave del dic de cada planta del json()
# posiblemente se cambie el for por un while
def catalogo(request,nombre_planta):

    dic = {"n_p" : nombre_planta} 
    for cosa in datos["data"]:
        if dic["n_p"] == cosa["common_name"]:
            ctx = cosa
        

    return render(request , "Catalogo.html" , ctx)
##

#
def listado(request):

    return render(request, "listado.html",datos)
#


def plantas(request):
    return render(request, "plantas.html")

def home(request):
    return render(request, "home.html")