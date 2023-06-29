from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets
from .models import Autores
from .models import Libro
from .models import Biblioteca
from .serializers import AutoresSerializer
from .serializers import LibroSerializer
from .serializers import BibliotecaSerializer
from rest_framework import generics

#MODELVIEWSET
class AutoresViewSet(viewsets.ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer

#GENERICAPIVIEW
class AutorCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset= Autores.objects.all()
    serializer_class=AutoresSerializer

class LibroCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset= Libro.objects.all()
    serializer_class=LibroSerializer

class BibliotecaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset= Biblioteca.objects.all()
    serializer_class=BibliotecaSerializer


#CUSTOM API
#@api_view(["GET"])

def autor_count(request):
    try:
        cantidad_autores=Autores.objects.count()
        return JsonResponse({
            "cantidad_autores": cantidad_autores
        },
        safe=False,
        status=200
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)
