# Generated by Django 4.2.3 on 2023-07-28 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0003_transacoes_valortotaldiario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacoes',
            name='dataTrans',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data da transação'),
        ),
    ]
