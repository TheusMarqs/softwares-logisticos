# Generated by Django 4.2.3 on 2023-07-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.IntegerField(),
        ),
    ]