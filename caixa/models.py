from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

class Transacoes(models.Model):
    choice_tipo = (
        ('E', 'Entrada'),
        ('S', 'Saída')
    )

    valor = models.FloatField(verbose_name='Valor')
    descricao = models.CharField(max_length=15, verbose_name='Descrição', null=True)
    tipo = models.CharField(max_length=1, choices=choice_tipo, verbose_name='Tipo')
    dataTrans = models.DateField(verbose_name='Data da transação', default=timezone.now)
    valorTotalDiario = models.FloatField(verbose_name='Valor Total Diário', default=0.0)
    valorTotalMensal = models.FloatField(verbose_name='Valor Total Mensal', default=0.0)

    def __str__(self):
        # Método para representação em string do objeto
        return f"{self.descricao} - {self.valor}"

@receiver(post_save, sender=Transacoes)
def atualizar_totais(sender, instance, **kwargs):
    # Calcula o valor total diário com base no tipo da transação
    transacoes_diarias = Transacoes.objects.filter(dataTrans=instance.dataTrans)
    total_diario = sum(transacao.valor for transacao in transacoes_diarias if transacao.tipo == 'E') - sum(transacao.valor for transacao in transacoes_diarias if transacao.tipo == 'S')

    # Calcula o valor total mensal com base no tipo da transação
    transacoes_mensais = Transacoes.objects.filter(dataTrans__month=instance.dataTrans.month)
    total_mensal = sum(transacao.valor for transacao in transacoes_mensais if transacao.tipo == 'E') - sum(transacao.valor for transacao in transacoes_mensais if transacao.tipo == 'S')

    instance.valorTotalDiario = total_diario
    instance.valorTotalMensal = total_mensal

    Transacoes.objects.filter(pk=instance.pk).update(valorTotalDiario=instance.valorTotalDiario, valorTotalMensal=instance.valorTotalMensal)
