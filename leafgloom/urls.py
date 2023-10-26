"""
URL configuration for leafgloom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from leafgloom.vistas import Pagina_inicial, catalogo, listado, plantas, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Pagina_inicial/",Pagina_inicial,),
    path("catalogo/<nombre_planta>", catalogo,),
    path("listado_de_plantas/",listado),
    path("plantas/",plantas),
    path("", home ),
]
