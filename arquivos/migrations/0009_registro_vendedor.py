# Generated by Django 4.2.3 on 2023-08-08 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arquivos', '0008_alter_registro_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='vendedor',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]