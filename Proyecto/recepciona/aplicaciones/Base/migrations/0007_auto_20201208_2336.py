# Generated by Django 2.2.13 on 2020-12-08 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0006_auto_20201208_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='comprobante',
            field=models.ImageField(blank=True, null=True, upload_to='comprobante/', verbose_name='Comprobante de pago'),
        ),
    ]
