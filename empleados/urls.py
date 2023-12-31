"""
URL configuration for empleados project.

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
from aplications.home.views import IndexView, ModeloPruebaListView 
from aplications.departamento.views import DepartametoListView
from aplications.empleado.views import EmpleadoDetailView
from aplications.articulos.views import ArticulosListView, ArticulosDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', IndexView.as_view()),
    path("lista_prueba/", ModeloPruebaListView.as_view()),
    path("Tabla_departamento/", DepartametoListView.as_view()),
    path("Lista_empleado/<pk>",EmpleadoDetailView.as_view()),
    path("Lista_Articulos/<pk>", ArticulosDetailView.as_view()),
]
