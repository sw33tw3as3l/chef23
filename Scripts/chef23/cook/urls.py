from django.urls import include, path
from django.shortcuts import render
from django.http import HttpResponse

from . import views

app_name = 'cook'

urlpatterns = [
    path('', views.home),
    path('<str:project_name>/add-new-vertex', views.add_vertex),
    path('<str:project_name>/add-new-edge', views.add_edge),
    path('<str:project_name>', views.graph),
]
