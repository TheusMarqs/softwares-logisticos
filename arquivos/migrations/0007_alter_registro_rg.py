# Generated by Django 4.2.3 on 2023-08-08 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivos', '0006_alter_registro_bairro_alter_registro_cidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='rg',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='RG/IE'),
        ),
    ]
