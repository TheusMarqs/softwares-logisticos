# Generated by Django 4.2.3 on 2023-07-28 17:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11, null=True, verbose_name='CPF/CNPJ')),
                ('email', models.EmailField(max_length=50, null=True)),
                ('rg', models.CharField(max_length=20, null=True, verbose_name='RG/IE')),
                ('cidade', models.CharField(max_length=25, null=True)),
                ('telefone', models.CharField(max_length=20, null=True)),
                ('numero', models.IntegerField(null=True, verbose_name='Número residencial')),
                ('rua', models.CharField(max_length=60, null=True)),
                ('bairro', models.CharField(max_length=20, null=True)),
                ('tipo', models.CharField(choices=[('P', 'Pedido'), ('O', 'Orçamento')], max_length=1)),
                ('data', models.DateField(default=django.utils.timezone.now, verbose_name='Data do pedido')),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField()),
                ('tamanho', models.FloatField()),
                ('valor_total', models.FloatField(default=0)),
                ('produto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produtos.produto')),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='arquivos.registro')),
            ],
        ),
    ]