from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Produto')
    valorCusto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor de custo')
    margemCusto = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Margem de lucro')
    valorVenda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Valor de venda')

    def save(self, *args, **kwargs):
        # Calculando o valorVenda antes de salvar o objeto
        self.valorVenda = self.valorCusto + (self.valorCusto * self.margemCusto / 100)
        super(Produto, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome