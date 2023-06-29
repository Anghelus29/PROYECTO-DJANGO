from rest_framework import serializers
from .models import Autores
from .models import Libro
from .models import Biblioteca

class AutoresSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Autores
        fields = "__all__"

class LibroSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Libro
        fields = "__all__"

class BibliotecaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Biblioteca
        fields = "__all__"