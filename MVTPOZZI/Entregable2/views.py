from django.http import HttpResponse
from django.shortcuts import render
from .models import familiares
# Create your views here.

def agrega(request,nombre,apellido,edad,parentes):
    familia=familiares(nombre=nombre,apellido=apellido,edad=edad,parentes=parentes)
    familia.save()
    return HttpResponse(f'<p>{familia.nombre} agregada/o con toda la otra info</p>')

def show_familia(request):
    lista=familiares.objects.all()
    
    return render(request, "familiares.html",{"show" : lista})


