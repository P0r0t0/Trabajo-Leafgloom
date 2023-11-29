from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render 
import requests

##      llaves
#   key = "sk-457k656529d1441692612"
#   key = "sk-FsEA653c5312682c42739"    
#   key = "sk-U5H76521de6713ac12231"
#   key = "sk-yl4e6521da2899f312380"
##
key = "sk-yl4e6521da2899f312380"
url1 = "https://perenual.com/api/species-list?key={}"
url2 = "https://perenual.com/api/species/details/{}?key={}"
response = requests.get(url1.format(key))
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

def catalogo(request, id):
    planta_id = requests.get(url2.format(id,key))
    ctx = planta_id.json()
 
    return render(request , "Catalogo.html" , ctx)
##

#
def listado(request):

    return render(request, "listado.html",datos)
#


def Lo_que_necesitas(request):
    return render(request, "Lo_que_necesitas.html")

def home(request):
    return render(request, "home.html")