from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"autores", views.AutoresViewSet)
router.register(r"libros", views.LibroViewSet)
router.register(r"bibliotecas", views.BibliotecaViewSet)


urlpatterns = [
    #path("", views.index, name="index"),
    path("autores_crear_listar", views.AutorCreateView.as_view(), name="autores_crear"),
    path("libros_crear_listar", views.LibroCreateView.as_view(), name="libros_crear"),
    path("bibliotecas_crear_listar", views.BibliotecaCreateView.as_view(), name="bibliotecas_crear"),

    path("autores/cantidad/", views.autor_count, name="autor_count"),

    path("", include(router.urls)),
]