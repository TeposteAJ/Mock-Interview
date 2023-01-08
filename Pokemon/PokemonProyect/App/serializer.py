#Primero se importan las librerias que nos permitiran crear clases que tengan las 
#propiedades de los serializadores 
#desde , por supesto el rest_Framework 
#¿Qué es un rest framework?
from rest_framework import serializers
#Además importamos del archivo donde se encuentran los modelos, pues los mismos modelos que creamos antes
from .models import (PokemonModel, TipoModel) 

#Ahora nuestra clase será de tipo serializador
#¿Qué es un serializador? 
class TipoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model= TipoModel
        fields = '__all__'

    def validate(self, attrs):
        return attrs

class PokemonSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PokemonModel
        fields = '__all__'

    def validate(self, attrs):
        return attrs
