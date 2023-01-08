from django.db import models

# Create your models here.

#Classe tipo modelo, para contener los tipos de pokemones que existen
class TipoModel(models.Model):
    type = models.CharField(max_length=50)
    # Solo tiene un campo este modelo que será el tipo de pokemon
    #además es un campo de tipo "CharField" para Texto corto
    #el id se generara de manera automatica
    
    class Meta:
        db_table = 'Tipo Pokemon'
         # esto nos permite configurar el nombre con el que aparecer este modelo en la BBD

# Classe tipo modelo, para contener los pokemones
class PokemonModel(models.Model):
    #campo tipo TExto corto, de maximo 50 caracteres, 
    #asigna el nombre del pokemon
    name = models.CharField(max_length=50)
    #campo tipo ForeingKey, se relacionará con el otro modeo de tipo de pokemon creada arriba
    #asignada mediante el id del tipo de pokemon, además es importante declarar que sucederá cuando se borre un tipo de pokemon,
    #CASCADE indica que se borrarán en automatico todos los pokemones almacenados que pertenecieran a ese tipo
    #null= True indica que esta permitido que se cree un pokemon con un campo de id nulo o que no tenga ningun tipo asignado
    tipo = models.ForeignKey(TipoModel, on_delete=models.CASCADE, null=True)
    #Campo de tipo fecha, para guardar cuando se cree el registro del pokemon 
    #auto_now_add --> que se creará de manera automatica
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.name 
    #Esto aun no me queda muy claro =/


