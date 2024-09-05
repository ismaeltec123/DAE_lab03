
from django.db import models
# Fecha : 2024-2
#Encargados : Juan León - Jaime Farfan
class Pregunta (models.Model):
    pregunta_texto=models.CharField(max_length=100)
    pub_date=models.DateField('fecha de publicacion')
class Opcion (models.Model):
    pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE) 
    opcion_texto=models.CharField(max_length=100) 
    votos=models.IntegerField(default=0)