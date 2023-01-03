from django.urls import path, include
from .views import (PokemonVista, TipoVista, PokemonVista2)

urlpatterns = [
    path('pokemon/', PokemonVista.as_view()),
    path('tipo/', TipoVista.as_view()),
    path('api/pokemon/<str:name>', PokemonVista2.as_view)
]
