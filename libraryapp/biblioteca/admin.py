from django.contrib import admin
from .models import Autores
from .models import Libro
from .models import Biblioteca
from .models import Biblioteca_libro

admin. site.register(Autores)
class AutorAdmin(admin.ModelAdmin):
    list_display=('id_autor','nombre', 'paginas', 'editorial')
    list_filter=('nombre','editorial')
    search_fields=('autores__nombre','nombre')
    ordering=('nombre','paginas')

class BibliotecaLibro(admin.ModelAdmin):
    list_display=('id_biblioteca_id', 'id_libro_id', 'disponible')


admin. site.register(Libro, AutorAdmin)
admin. site.register(Biblioteca)
admin. site.register(Biblioteca_libro, BibliotecaLibro)