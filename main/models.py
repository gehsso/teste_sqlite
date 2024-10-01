from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15,verbose_name="C.P.F")


    def __str__(self):
        return self.nome