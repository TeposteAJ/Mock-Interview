from django.db import models

# Create your models here.

#Classe tipo modelo
class TipoModel(models.Model):
    type = models.CharField(max_length=50)
    # Solo tiene un campo este modelo que será el tipo de pokemon
    
    class Meta:
        db_table = 'Tipo Pokemon'
         # esto nos permite configurar el nombre con el que aparecer este modelo en la BBD


class PokemonModel(models.Model):
    name = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoModel, on_delete=models.CASCADE, null=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name 


