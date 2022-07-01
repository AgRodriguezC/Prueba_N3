from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=30)
    rut= models.CharField(max_length=12)
    apPaterno= models.CharField(max_length=30)
    apMaterno= models.CharField(max_length=30)
    edad= models.IntegerField()
    vacuna= models.CharField(max_length=30)
    fecha =models.DateField()
    