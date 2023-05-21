from django.shortcuts import render
from .models import Contacto, Descarga, Bloc, Temporada

# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')


def temporada(request):
    temporada=Temporada.objects.all()
    return render(request, 'temporada.html',{'temporadas': temporada})


def descarga(request):
    descarga=Descarga.objects.all()
    return render(request, 'descarga.html',{'descargas': descarga})

def bloc(request):
    bloc = Bloc.objects.all()
    return render(request, 'bloc.html',{"blocs": bloc})

def contacto(request):
    perfil = Contacto.objects.first()
    return render(request , 'contacto.html', {'perfil': perfil})