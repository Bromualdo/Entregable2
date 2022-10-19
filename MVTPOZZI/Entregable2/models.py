from asyncio.windows_events import NULL
from django.db import models
from datetime import datetime
# Create your models here.
class familiares (models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    parentes=models.CharField(max_length=50)
    nac=models.DateField(null=True)