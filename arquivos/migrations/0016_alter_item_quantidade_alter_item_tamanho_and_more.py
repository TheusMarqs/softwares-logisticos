# Generated by Django 4.2.3 on 2023-08-09 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivos', '0015_alter_item_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantidade',
            field=models.IntegerField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='tamanho',
            field=models.IntegerField(blank=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='valor_total',
            field=models.IntegerField(blank=True, default=0, verbose_name=''),
        ),
    ]