# Generated by Django 2.2.13 on 2020-12-08 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_auto_20201130_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='comprobante',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Comprobante de pago'),
        ),
    ]
