from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializer import PokemonSerializer, TipoSerializer

# Create your views here.
class PokemonVista (APIView): 
    def post(self, request): 
        serializer= PokemonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class PokemonVista2 (APIView): 
    def get(self,request,name):
        pass


        


class TipoVista (APIView): 
    def post(self, request): 
        serializer= TipoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
