# Generated by Django 2.2.13 on 2020-11-30 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regiones',
            fields=[
                ('region_id', models.AutoField(primary_key=True, serialize=False)),
                ('region_nombre', models.CharField(max_length=100, verbose_name='Nombre region')),
                ('region_ordinal', models.CharField(max_length=4, verbose_name='Region ordinal')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('provincia_id', models.AutoField(primary_key=True, serialize=False)),
                ('provincia_nombre', models.CharField(max_length=100, verbose_name='Nombre provincia')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.Regiones')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Comunas',
            fields=[
                ('comuna_id', models.AutoField(primary_key=True, serialize=False)),
                ('comuna_nombre', models.CharField(max_length=100, verbose_name='Nombre comuna')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.Provincias')),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
            },
        ),
    ]
