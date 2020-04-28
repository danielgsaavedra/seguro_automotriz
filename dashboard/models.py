from django.db import models

# Create your models here.


class Asegurado(models.Model):
    rut_asegurado = models.CharField(primary_key=True, max_length=12)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apeliido = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    fecha_nacimiento = models.DateField()
    usuario_rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario')

    class Meta:
        managed = False
        db_table = 'asegurado'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    region_nro_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_nro_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class Direccion(models.Model):
    id_direccion = models.IntegerField(primary_key=True)
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')
    usuario_rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', blank=True, null=True)
    asegurado_rut_asegurado = models.ForeignKey(Asegurado, models.DO_NOTHING, db_column='asegurado_rut_asegurado', blank=True, null=True)
    servicio_grua_id_servicio = models.ForeignKey('ServicioGrua', models.DO_NOTHING, db_column='servicio_grua_id_servicio', blank=True, null=True)       
    siniestro_nro_siniestro = models.ForeignKey('Siniestro', models.DO_NOTHING, db_column='siniestro_nro_siniestro', blank=True, null=True)
    taller_id_taller = models.ForeignKey('Taller', models.DO_NOTHING, db_column='taller_id_taller', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class EstadoPresupuesto(models.Model):
    id_est_presupuesto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_presupuesto'


class EstadoSiniestro(models.Model):
    id_est_siniestro = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_siniestro'


class FormularioActa(models.Model):
    id_acta = models.IntegerField(primary_key=True)
    fecha_hora = models.DateField()
    observaciones = models.CharField(max_length=300, blank=True, null=True)
    tipo_acta_id_tipo_acta = models.ForeignKey('TipoActa', models.DO_NOTHING, db_column='tipo_acta_id_tipo_acta')
    siniestro_nro_siniestro = models.ForeignKey('Siniestro', models.DO_NOTHING, db_column='siniestro_nro_siniestro')
    taller_id_taller = models.ForeignKey('Taller', models.DO_NOTHING, db_column='taller_id_taller')
    usuario_rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario')

    class Meta:
        managed = False
        db_table = 'formulario_acta'


class Grua(models.Model):
    patente_grua = models.CharField(primary_key=True, max_length=10)
    estado = models.CharField(max_length=1)
    servicio_grua_id_servicio = models.ForeignKey('ServicioGrua', models.DO_NOTHING, db_column='servicio_grua_id_servicio')
    usuario_rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario')

    class Meta:
        managed = False
        db_table = 'grua'


class InformeDano(models.Model):
    id_info_dano = models.IntegerField(primary_key=True)
    fecha_hora = models.DateField()
    observaciones = models.CharField(max_length=500)
    perdida_total = models.CharField(max_length=1, blank=True, null=True)
    tipo_dano_id_tipo_dano = models.ForeignKey('TipoDano', models.DO_NOTHING, db_column='tipo_dano_id_tipo_dano')
    severidad_dano_id_seve_dano = models.ForeignKey('SeveridadDano', models.DO_NOTHING, db_column='severidad_dano_id_seve_dano')
    vehiculo_patente_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente_vehiculo')
    taller_id_taller = models.ForeignKey('Taller', models.DO_NOTHING, db_column='taller_id_taller')
    siniestro_nro_siniestro = models.ForeignKey('Siniestro', models.DO_NOTHING, db_column='siniestro_nro_siniestro')
    usuario_rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario')

    class Meta:
        managed = False
        db_table = 'informe_dano'


class Marca(models.Model):
    id_marca = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'marca'


class PlanSeguro(models.Model):
    id_plan_seguro = models.IntegerField(primary_key=True)
    tipo_plan_id_tip_plan = models.ForeignKey('TipoPlan', models.DO_NOTHING, db_column='tipo_plan_id_tip_plan')
    poliza_id_poliza = models.ForeignKey('Poliza', models.DO_NOTHING, db_column='poliza_id_poliza')
    deducible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plan_seguro'


class Poliza(models.Model):
    id_poliza = models.IntegerField(primary_key=True)
    vigente = models.CharField(max_length=1)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    firma = models.CharField(max_length=200)
    asegurado_rut_asegurado = models.ForeignKey(Asegurado, models.DO_NOTHING, db_column='asegurado_rut_asegurado')
    vehiculo_patente_vehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente_vehiculo')

    class Meta:
        managed = False
        db_table = 'poliza'


class Presupuesto(models.Model):
    id_presupuesto = models.IntegerField(primary_key=True)
    fecha_hora = models.DateField()
    valor_total = models.IntegerField()
    estado_id_est_presupuesto = models.ForeignKey(EstadoPresupuesto, models.DO_NOTHING, db_column='estado_id_est_presupuesto')
    usuario_rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', blank=True, null=True)
    informe_dano_id_info_dano = models.ForeignKey(InformeDano, models.DO_NOTHING, db_column='informe_dano_id_info_dano')

    class Meta:
        managed = False
        db_table = 'presupuesto'


class RegAsegurado(models.Model):
    id_reg_asegurado = models.IntegerField(primary_key=True)
    nombre_registrador = models.CharField(max_length=30)
    nombre_asegurado = models.CharField(max_length=30)
    nro_poliza = models.IntegerField()
    fecha_hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'reg_asegurado'


class RegError(models.Model):
    id_error = models.IntegerField(primary_key=True)
    error = models.CharField(max_length=50)
    cod_error = models.CharField(max_length=500)
    mensaje = models.CharField(max_length=300)
    fecha_hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'reg_error'


class RegGrua(models.Model):
    id_reg_grua = models.FloatField(primary_key=True)
    nombre_registrador = models.CharField(max_length=30)
    patente_grua = models.CharField(max_length=7)
    fecha_hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'reg_grua'


class RegPoliza(models.Model):
    id_reg_poliza = models.IntegerField(primary_key=True)
    nombre_registrador = models.CharField(max_length=30)
    nro_poliza = models.IntegerField()
    fecha_hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'reg_poliza'


class RegSiniestro(models.Model):
    id_reg_siniestro = models.IntegerField(primary_key=True)
    nombre_registrador = models.CharField(max_length=30)
    nro_siniestro = models.IntegerField()
    fecha_hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'reg_siniestro'


class RegTaller(models.Model):
    id_reg_taller = models.IntegerField(primary_key=True)
    nombre_registrador = models.CharField(max_length=30)
    nombre_taller = models.CharField(max_length=30)
    fecha_hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'reg_taller'


class RegUsuario(models.Model):
    id_reg_usuario = models.IntegerField(primary_key=True)
    nombre_registrador = models.CharField(max_length=30)
    nombre_registrado = models.CharField(max_length=30)
    fecha_hora = models.DateField()

    class Meta:
        managed = False
        db_table = 'reg_usuario'


class Region(models.Model):
    nro_region = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    tipo_rol = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'rol'


class ServicioGrua(models.Model):
    id_servicio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=400)
    razon_social = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=50)
    usuario_rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario')

    class Meta:
        managed = False
        db_table = 'servicio_grua'


class SeveridadDano(models.Model):
    id_seve_dano = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'severidad_dano'


class Siniestro(models.Model):
    nro_siniestro = models.CharField(primary_key=True, max_length=10)
    fecha_hr = models.DateField()
    descripcion = models.CharField(max_length=100)
    parte_policial = models.CharField(max_length=100, blank=True, null=True)
    foto_licencia = models.CharField(max_length=100, blank=True, null=True)
    tipo_accidente_id_tipo_acc = models.ForeignKey('TipoAccidente', models.DO_NOTHING, db_column='tipo_accidente_id_tipo_acc')
    est_siniestro_id_est_siniestro = models.ForeignKey(EstadoSiniestro, models.DO_NOTHING, db_column='est_siniestro_id_est_siniestro')
    taller_id_taller = models.ForeignKey('Taller', models.DO_NOTHING, db_column='taller_id_taller')
    grua_patente_grua = models.ForeignKey(Grua, models.DO_NOTHING, db_column='grua_patente_grua', blank=True, null=True)
    usuario_rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario')
    poliza_id_poliza = models.ForeignKey(Poliza, models.DO_NOTHING, db_column='poliza_id_poliza')

    class Meta:
        managed = False
        db_table = 'siniestro'


class Taller(models.Model):
    id_taller = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    razon_social = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=30)
    capacidad_taller = models.IntegerField()
    estado = models.CharField(max_length=1)
    usuario_rut_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario')

    class Meta:
        managed = False
        db_table = 'taller'


class TipoAccidente(models.Model):
    id_tipo_acc = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_accidente'


class TipoActa(models.Model):
    id_tipo_acta = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'tipo_acta'


class TipoDano(models.Model):
    id_tipo_dano = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'tipo_dano'


class TipoPlan(models.Model):
    id_tip_plan = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=500)
    valor = models.IntegerField()
    cobertura_max = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_plan'


class TipoVehiculo(models.Model):
    id_tipo_auto = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_vehiculo'


class Usuario(models.Model):
    rut_usuario = models.CharField(primary_key=True, max_length=12)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    telefono = models.BigIntegerField()
    rol_id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol_id_rol')

    class Meta:
        managed = False
        db_table = 'usuario'


class Vehiculo(models.Model):
    patente_vehiculo = models.CharField(primary_key=True, max_length=8)
    anio = models.IntegerField()
    modelo = models.CharField(max_length=200)
    nro_motor = models.CharField(max_length=100)
    tipo_vehiculo_id_tipo_auto = models.ForeignKey(TipoVehiculo, models.DO_NOTHING, db_column='tipo_vehiculo_id_tipo_auto')
    marca_id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='marca_id_marca')
    asegurado_rut_asegurado = models.ForeignKey(Asegurado, models.DO_NOTHING, db_column='asegurado_rut_asegurado')

    class Meta:
        managed = False
        db_table = 'vehiculo'