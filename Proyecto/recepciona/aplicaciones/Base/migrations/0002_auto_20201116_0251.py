# Generated by Django 2.2.13 on 2020-11-16 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='horario',
            name='cancha',
        ),
        migrations.AddField(
            model_name='tipo_cancha',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='deporte_img/', verbose_name='Deporte'),
        ),
        migrations.AlterField(
            model_name='cancha',
            name='imagen',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='cancha_img/', verbose_name='Imagen principal'),
        ),
    ]
