from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, verbose_name='CPF/CNPJ')
    email = models.EmailField(max_length=50, null=True)
    rg = models.CharField(max_length=20, null=True)
    cidade = models.CharField(max_length=25)
    telefone = models.CharField(max_length=20)
    numero = models.IntegerField()
    rua = models.CharField(max_length=60, null=True)
    bairro = models.CharField(max_length=20)

    def __str__(self):
        return self.nome