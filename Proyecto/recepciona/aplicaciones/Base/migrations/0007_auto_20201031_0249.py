# Generated by Django 2.2.13 on 2020-10-31 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0006_auto_20201026_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='date_end',
            field=models.CharField(max_length=20, verbose_name='date_end'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='date_start',
            field=models.CharField(max_length=20, verbose_name='date_start'),
        ),
    ]
