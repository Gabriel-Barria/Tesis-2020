# Generated by Django 2.2.13 on 2020-12-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_reserva_comprobante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.BooleanField(default=False, verbose_name='Estado'),
        ),
    ]