# Generated by Django 3.0.5 on 2020-04-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asegurado',
            fields=[
                ('rut_asegurado', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(max_length=20)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apeliido', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
            options={
                'db_table': 'asegurado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.IntegerField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
            ],
            options={
                'db_table': 'direccion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoPresupuesto',
            fields=[
                ('id_est_presupuesto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'estado_presupuesto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoSiniestro',
            fields=[
                ('id_est_siniestro', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'estado_siniestro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormularioActa',
            fields=[
                ('id_acta', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_hora', models.DateField()),
                ('observaciones', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'formulario_acta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Grua',
            fields=[
                ('patente_grua', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'grua',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InformeDano',
            fields=[
                ('id_info_dano', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_hora', models.DateField()),
                ('observaciones', models.CharField(max_length=500)),
                ('perdida_total', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'informe_dano',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'marca',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlanSeguro',
            fields=[
                ('id_plan_seguro', models.IntegerField(primary_key=True, serialize=False)),
                ('deducible', models.IntegerField()),
            ],
            options={
                'db_table': 'plan_seguro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Poliza',
            fields=[
                ('id_poliza', models.IntegerField(primary_key=True, serialize=False)),
                ('vigente', models.CharField(max_length=1)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('firma', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'poliza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id_presupuesto', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha_hora', models.DateField()),
                ('valor_total', models.IntegerField()),
            ],
            options={
                'db_table': 'presupuesto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegAsegurado',
            fields=[
                ('id_reg_asegurado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_registrador', models.CharField(max_length=30)),
                ('nombre_asegurado', models.CharField(max_length=30)),
                ('nro_poliza', models.IntegerField()),
                ('fecha_hora', models.DateField()),
            ],
            options={
                'db_table': 'reg_asegurado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegError',
            fields=[
                ('id_error', models.IntegerField(primary_key=True, serialize=False)),
                ('error', models.CharField(max_length=50)),
                ('cod_error', models.CharField(max_length=500)),
                ('mensaje', models.CharField(max_length=300)),
                ('fecha_hora', models.DateField()),
            ],
            options={
                'db_table': 'reg_error',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegGrua',
            fields=[
                ('id_reg_grua', models.FloatField(primary_key=True, serialize=False)),
                ('nombre_registrador', models.CharField(max_length=30)),
                ('patente_grua', models.CharField(max_length=7)),
                ('fecha_hora', models.DateField()),
            ],
            options={
                'db_table': 'reg_grua',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('nro_region', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegPoliza',
            fields=[
                ('id_reg_poliza', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_registrador', models.CharField(max_length=30)),
                ('nro_poliza', models.IntegerField()),
                ('fecha_hora', models.DateField()),
            ],
            options={
                'db_table': 'reg_poliza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegSiniestro',
            fields=[
                ('id_reg_siniestro', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_registrador', models.CharField(max_length=30)),
                ('nro_siniestro', models.IntegerField()),
                ('fecha_hora', models.DateField()),
            ],
            options={
                'db_table': 'reg_siniestro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegTaller',
            fields=[
                ('id_reg_taller', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_registrador', models.CharField(max_length=30)),
                ('nombre_taller', models.CharField(max_length=30)),
                ('fecha_hora', models.DateField()),
            ],
            options={
                'db_table': 'reg_taller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegUsuario',
            fields=[
                ('id_reg_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_registrador', models.CharField(max_length=30)),
                ('nombre_registrado', models.CharField(max_length=30)),
                ('fecha_hora', models.DateField()),
            ],
            options={
                'db_table': 'reg_usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_rol', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ServicioGrua',
            fields=[
                ('id_servicio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=400)),
                ('razon_social', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('correo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'servicio_grua',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SeveridadDano',
            fields=[
                ('id_seve_dano', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'severidad_dano',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Siniestro',
            fields=[
                ('nro_siniestro', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('fecha_hr', models.DateField()),
                ('descripcion', models.CharField(max_length=100)),
                ('parte_policial', models.CharField(blank=True, max_length=100, null=True)),
                ('foto_licencia', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'siniestro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id_taller', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('razon_social', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
                ('correo', models.CharField(max_length=30)),
                ('capacidad_taller', models.IntegerField()),
                ('estado', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'taller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoAccidente',
            fields=[
                ('id_tipo_acc', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipo_accidente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoActa',
            fields=[
                ('id_tipo_acta', models.FloatField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'tipo_acta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoDano',
            fields=[
                ('id_tipo_dano', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'tipo_dano',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPlan',
            fields=[
                ('id_tip_plan', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=500)),
                ('valor', models.IntegerField()),
                ('cobertura_max', models.IntegerField()),
            ],
            options={
                'db_table': 'tipo_plan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoVehiculo',
            fields=[
                ('id_tipo_auto', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_vehiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut_usuario', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=20)),
                ('segundo_nombre', models.CharField(max_length=20)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente_vehiculo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('anio', models.IntegerField()),
                ('modelo', models.CharField(max_length=200)),
                ('nro_motor', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
    ]
