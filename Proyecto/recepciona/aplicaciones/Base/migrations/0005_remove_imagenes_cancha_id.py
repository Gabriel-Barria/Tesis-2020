# Generated by Django 2.2.13 on 2020-11-29 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_auto_20201129_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenes',
            name='cancha_id',
        ),
    ]
