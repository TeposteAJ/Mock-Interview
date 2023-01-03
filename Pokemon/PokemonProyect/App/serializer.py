from rest_framework import serializers

from .models import (PokemonModel, TipoModel) 


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