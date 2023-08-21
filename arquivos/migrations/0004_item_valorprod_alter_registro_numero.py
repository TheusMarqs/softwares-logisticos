# Generated by Django 4.2.3 on 2023-08-07 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivos', '0003_alter_registro_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='valorProd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registro',
            name='numero',
            field=models.TextField(null=True, verbose_name='Número residencial'),
        ),
    ]
