# Generated by Django 2.2.13 on 2020-09-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]