from django.db import models

class Candidato(models.Model):
    
    nombre = models.CharField(max_length=50)  
    apellido = models.CharField(max_length=50)  
    ciudad = models.CharField(max_length=100)  
    telefono = models.CharField(max_length=15)  
    dni = models.CharField(max_length=20)  


