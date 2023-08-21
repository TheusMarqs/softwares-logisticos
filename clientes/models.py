from django.db import models
import json

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, verbose_name='CPF/CNPJ')
    email = models.EmailField(max_length=50, null=True, blank=True, default='')
    rg = models.CharField(max_length=20, null=True, blank=True, default='')
    cidade = models.CharField(max_length=25)
    telefone = models.CharField(max_length=20)
    numero = models.CharField(max_length=10)
    rua = models.CharField(max_length=60, null=True, blank=True, default='')
    bairro = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    def to_json(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'rg': self.rg,
            'cidade': self.cidade,
            'telefone': self.telefone,
            'numero': self.numero,
            'rua': self.rua,
            'bairro': self.bairro,
        }
        