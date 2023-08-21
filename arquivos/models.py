from django.db import models
from django.utils import timezone
import datetime
from clientes.models import Cliente
from produtos.models import Produto

class Registro(models.Model):
    choice_tipo = (
        ('P', 'Pedido'),
        ('O', 'Orçamento')
    )

    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, verbose_name='CPF/CNPJ', null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    rg = models.CharField(max_length=20, null=True, verbose_name='RG/IE', blank=True)
    cidade = models.CharField(max_length=25, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    numero = models.CharField(max_length=10, verbose_name='Número residencial', null=True, blank=True)
    rua = models.CharField(max_length=60, null=True, blank=True)
    bairro = models.CharField(max_length=20, null=True, blank=True)
    tipo = models.CharField(max_length=1, choices=choice_tipo)
    vendedor = models.CharField(max_length=15, null=True, blank=True)
    data = models.DateField(verbose_name="Data do registro", default=datetime.datetime.now)
    totalPedido = models.FloatField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome

class Item(models.Model):
    quantidade = models.FloatField(verbose_name='', null=True, blank=True)
    tamanho = models.CharField(max_length=10, verbose_name='', null=True, blank=True)
    valorProd = models.FloatField(null=True, blank=True, verbose_name='')
    totalProd = models.FloatField(verbose_name='', null=True, blank=True)
    registro = models.ForeignKey(Registro, on_delete=models.SET_NULL, null=True)
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True)