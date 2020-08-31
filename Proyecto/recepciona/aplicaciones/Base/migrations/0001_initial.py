# Generated by Django 2.2.13 on 2020-08-30 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cancha',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=40, verbose_name='Descripcion')),
                ('direccion', models.CharField(max_length=40, verbose_name='Direccion')),
                ('valor', models.CharField(max_length=40, verbose_name='Valor hora')),
            ],
            options={
                'verbose_name': 'Cancha',
                'verbose_name_plural': 'Canchas',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_comuna', models.CharField(max_length=40, verbose_name='Nombre comuna')),
            ],
            options={
                'verbose_name': 'Comuna',
                'verbose_name_plural': 'Comunas',
            },
        ),
        migrations.CreateModel(
            name='Dias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, verbose_name='Dia')),
            ],
            options={
                'verbose_name': 'Dia',
                'verbose_name_plural': 'Dias',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100, verbose_name='Calle')),
                ('numero', models.IntegerField(verbose_name='Numero')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.Comuna')),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=40, verbose_name='Nombre region')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regiones',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.CreateModel(
            name='Superficie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Superficie',
                'verbose_name_plural': 'Superficies',
            },
        ),
        migrations.CreateModel(
            name='Tipo_cancha',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de cancha',
                'verbose_name_plural': 'Tipos de canchas',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=40, verbose_name='Nombres')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('contrasenia', models.CharField(max_length=40, verbose_name='Contraseña')),
                ('apellidop', models.CharField(max_length=40, verbose_name='Apellido paterno')),
                ('apellidom', models.CharField(max_length=40, verbose_name='Apellido materno')),
                ('direccion_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.Direccion')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.Roles')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='reserva',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hora_inicio', models.TimeField(verbose_name='Desde')),
                ('hora_fin', models.TimeField(verbose_name='Hasta')),
                ('fecha_reserva', models.DateField(verbose_name='Fecha de reserva')),
                ('Cancha_r', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.cancha')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.Usuario')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hora_inicio', models.TimeField(verbose_name='hora inicio')),
                ('hora_termino', models.TimeField(verbose_name='hora termino')),
                ('cancha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.cancha')),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.Dias')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
            },
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.Region'),
        ),
        migrations.AddField(
            model_name='cancha',
            name='servicios',
            field=models.ManyToManyField(to='Base.Servicio'),
        ),
        migrations.AddField(
            model_name='cancha',
            name='superfice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.Superficie'),
        ),
        migrations.AddField(
            model_name='cancha',
            name='tipo_cancha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.Tipo_cancha'),
        ),
        migrations.AddField(
            model_name='cancha',
            name='usuario_cancha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Base.Usuario'),
        ),
    ]
