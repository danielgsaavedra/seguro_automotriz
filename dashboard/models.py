# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asegurado(models.Model):
    rut_asegurado = models.CharField(
        primary_key=True, max_length=12, verbose_name='Rut')
    primer_nombre = models.CharField(
        max_length=20, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(
        max_length=20, verbose_name='Segundo Nombre')
    primer_apellido = models.CharField(
        max_length=20, verbose_name='Apellido Paterno')
    segundo_apeliido = models.CharField(
        max_length=20, verbose_name='Apellido Materno')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    telefono = models.BigIntegerField(verbose_name='Teléfono')
    fecha_nacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    estado = models.CharField(max_length=1,default=1)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario')

    class Meta:
        managed = False
        db_table = 'asegurado'

        verbose_name_plural = 'Asegurados'

    def __str__(self):
        return self.rut_asegurado


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(
        unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True, verbose_name='ID Comuna')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    region_nro_region = models.ForeignKey(
        'Region', models.DO_NOTHING, db_column='region_nro_region', verbose_name='Región')

    class Meta:
        managed = False
        db_table = 'comuna'
        verbose_name_plural = 'Comuna'

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    id_direccion = models.IntegerField(
        primary_key=True, verbose_name='ID Dirección')
    calle = models.CharField(max_length=50, verbose_name='Calle')
    numero = models.IntegerField(verbose_name='N°')
    comuna_id_comuna = models.ForeignKey(
        Comuna, models.DO_NOTHING, db_column='comuna_id_comuna', verbose_name='Comuna')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', blank=True, null=True, verbose_name='Rut Usuario')
    asegurado_rut_asegurado = models.ForeignKey(
        Asegurado, models.DO_NOTHING, db_column='asegurado_rut_asegurado', blank=True, null=True, verbose_name='Asegurado')
    servicio_grua_id_servicio = models.ForeignKey(
        'ServicioGrua', models.DO_NOTHING, db_column='servicio_grua_id_servicio', blank=True, null=True, verbose_name='Servicio GRúa')
    siniestro_nro_siniestro = models.ForeignKey(
        'Siniestro', models.DO_NOTHING, db_column='siniestro_nro_siniestro', blank=True, null=True, verbose_name='N° Siniestro')
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', blank=True, null=True, verbose_name='Taller')

    class Meta:
        managed = False
        db_table = 'direccion'
        verbose_name_plural = 'Direcciones'

    def __str__(self):
        return self.calle + ' ' + '#' + str(self.numero)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstadoPresupuesto(models.Model):
    id_est_presupuesto = models.IntegerField(
        primary_key=True, verbose_name='ID Est. Presupuesto')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')

    class Meta:
        managed = False
        db_table = 'estado_presupuesto'
        verbose_name_plural = 'Estado Presupuestos'

    def __str__(self):
        return self.nombre


class EstadoSiniestro(models.Model):
    id_est_siniestro = models.IntegerField(
        primary_key=True, verbose_name='ID Est. Siniestro')
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')

    class Meta:
        managed = False
        db_table = 'estado_siniestro'
        verbose_name_plural = 'Estado Siniestros'

    def __str__(self):
        return self.nombre


class FormularioActa(models.Model):
    id_acta = models.IntegerField(primary_key=True, verbose_name='ID Acta')
    fecha_hora = models.DateField(verbose_name='Fecha')
    observaciones = models.CharField(
        max_length=300, blank=True, null=True, verbose_name='Observaciones')
    tipo_acta_id_tipo_acta = models.ForeignKey(
        'TipoActa', models.DO_NOTHING, db_column='tipo_acta_id_tipo_acta', verbose_name='Tipo Acta')
    siniestro_nro_siniestro = models.ForeignKey(
        'Siniestro', models.DO_NOTHING, db_column='siniestro_nro_siniestro', verbose_name='ID Siniestro')
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario')

    class Meta:
        managed = False
        db_table = 'formulario_acta'
        verbose_name_plural = 'Formulario Actas'

    def __str__(self):
        return str(self.id_acta)


class Grua(models.Model):
    patente_grua = models.CharField(
        primary_key=True, max_length=10, verbose_name='Patente Grúa')
    estado = models.CharField(max_length=1, verbose_name='Estado')
    servicio_grua_id_servicio = models.ForeignKey(
        'ServicioGrua', models.DO_NOTHING, db_column='servicio_grua_id_servicio', verbose_name='Servicio Grúa')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario')

    class Meta:
        managed = False
        db_table = 'grua'
        verbose_name_plural = 'Grúas'

    def __str__(self):
        return self.patente_grua


class InformeDano(models.Model):
    id_info_dano = models.IntegerField(
        primary_key=True, verbose_name='ID Inf. Daño')
    fecha_hora = models.DateField(verbose_name='Fecha')
    observaciones = models.CharField(
        max_length=500, verbose_name='Observaciones')
    perdida_total = models.CharField(
        max_length=1, blank=True, null=True, verbose_name='Perdida Total')
    tipo_dano_id_tipo_dano = models.ForeignKey(
        'TipoDano', models.DO_NOTHING, db_column='tipo_dano_id_tipo_dano', verbose_name='Tipo Daño')
    severidad_dano_id_seve_dano = models.ForeignKey(
        'SeveridadDano', models.DO_NOTHING, db_column='severidad_dano_id_seve_dano', verbose_name='Severidad Daño')
    vehiculo_patente_vehiculo = models.ForeignKey(
        'Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente_vehiculo', verbose_name='Patente Vehículo')
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller')
    siniestro_nro_siniestro = models.ForeignKey(
        'Siniestro', models.DO_NOTHING, db_column='siniestro_nro_siniestro', verbose_name='ID Siniestro')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario')

    class Meta:
        managed = False
        db_table = 'informe_dano'
        verbose_name_plural = 'Informe Daños'

    def __str__(self):
        return str(self.id_info_dano)


class Marca(models.Model):
    id_marca = models.BigIntegerField(
        primary_key=True, verbose_name='ID Marca')
    nombre = models.CharField(max_length=20, verbose_name='Nombre Marca')

    class Meta:
        managed = False
        db_table = 'marca'

    def __str__(self):
        return str(self.nombre)


class PlanSeguro(models.Model):
    id_plan_seguro = models.IntegerField(
        primary_key=True, verbose_name='ID Plan')
    tipo_plan_id_tip_plan = models.ForeignKey(
        'TipoPlan', models.DO_NOTHING, db_column='tipo_plan_id_tip_plan', verbose_name='Tipo Plan')
    poliza_id_poliza = models.ForeignKey(
        'Poliza', models.DO_NOTHING, db_column='poliza_id_poliza', verbose_name='ID Póliza')
    deducible = models.IntegerField(verbose_name='Deducible')

    class Meta:
        managed = False
        db_table = 'plan_seguro'
        unique_together = (('tipo_plan_id_tip_plan', 'poliza_id_poliza'),)
        verbose_name_plural = 'Plan Seguros'

    def __str__(self):
        return str(self.tipo_plan_id_tip_plan)


class Poliza(models.Model):
    id_poliza = models.IntegerField(primary_key=True, verbose_name='ID Póliza')
    vigente = models.CharField(max_length=1, verbose_name='Vigencia')
    fecha_inicio = models.DateField(verbose_name='Fecha Inicio')
    fecha_fin = models.DateField(verbose_name='Fecha Termino')
    firma = models.CharField(max_length=200, verbose_name='Firma')
    estado = models.CharField(max_length=1,default=1)
    asegurado_rut_asegurado = models.ForeignKey(
        Asegurado, models.DO_NOTHING, db_column='asegurado_rut_asegurado', verbose_name='Rut Asegurado')
    vehiculo_patente_vehiculo = models.ForeignKey(
        'Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente_vehiculo', verbose_name='Patente Vehículo')

    class Meta:
        managed = False
        db_table = 'poliza'
        verbose_name_plural = 'Pólizas'

    def __str__(self):
        return str(self.id_poliza)


class Presupuesto(models.Model):
    id_presupuesto = models.IntegerField(
        primary_key=True, verbose_name='ID Presupuestos')
    fecha_hora = models.DateField(verbose_name='Fecha')
    valor_total = models.IntegerField(verbose_name='Valor Total')
    estado_id_est_presupuesto = models.ForeignKey(
        EstadoPresupuesto, models.DO_NOTHING, db_column='estado_id_est_presupuesto', verbose_name='ID Est. Presupuesto')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', blank=True, null=True, verbose_name='Rut Usuario')
    informe_dano_id_info_dano = models.ForeignKey(
        InformeDano, models.DO_NOTHING, db_column='informe_dano_id_info_dano', verbose_name='ID Inf. Daño')

    class Meta:
        managed = False
        db_table = 'presupuesto'
        verbose_name_plural = 'Presupuestos'

    def __str__(self):
        return str(self.id_presupuesto) + ' ' + str(self.valor_total)


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
    nro_region = models.IntegerField(
        primary_key=True, verbose_name='N° Región')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Región')

    class Meta:
        managed = False
        db_table = 'region'
        verbose_name_plural = 'Regiones'

    def __str__(self):
        return self.nombre


class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True, verbose_name='ID Rol')
    tipo_rol = models.CharField(max_length=20, verbose_name='Tipo Rol')

    class Meta:
        managed = False
        db_table = 'rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return str(self.id_rol)


class ServicioGrua(models.Model):
    id_servicio = models.IntegerField(
        primary_key=True, verbose_name='ID Servicio')
    nombre = models.CharField(max_length=400, verbose_name='Nombre')
    razon_social = models.CharField(max_length=50, verbose_name='Razón Social')
    telefono = models.BigIntegerField(verbose_name='Teléfono')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario')

    class Meta:
        managed = False
        db_table = 'servicio_grua'
        verbose_name_plural = 'Servicios Grúas'

    def __str__(self):
        return self.nombre


class SeveridadDano(models.Model):
    id_seve_dano = models.IntegerField(
        primary_key=True, verbose_name='ID Sev. Daños')
    nombre = models.CharField(max_length=50, verbose_name='Nombre ')

    class Meta:
        managed = False
        db_table = 'severidad_dano'
        verbose_name_plural = 'Severidad Daños'

    def __str__(self):
        return self.nombre


class Siniestro(models.Model):
    nro_siniestro = models.CharField(
        primary_key=True, max_length=10, verbose_name='N° Siniestro')
    fecha_hr = models.DateField(verbose_name='Fecha Siniestro')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')
    parte_policial = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Parte Policial')
    foto_licencia = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Foto Licencia')
    tipo_accidente_id_tipo_acc = models.ForeignKey(
        'TipoAccidente', models.DO_NOTHING, db_column='tipo_accidente_id_tipo_acc', verbose_name='Tipo Accidente')
    est_siniestro_id_est_siniestro = models.ForeignKey(
        EstadoSiniestro, models.DO_NOTHING, db_column='est_siniestro_id_est_siniestro', verbose_name='Estado Siniestro')
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller')
    grua_patente_grua = models.ForeignKey(
        Grua, models.DO_NOTHING, db_column='grua_patente_grua', blank=True, null=True, verbose_name='Patente Grúa')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario')
    poliza_id_poliza = models.ForeignKey(
        Poliza, models.DO_NOTHING, db_column='poliza_id_poliza', verbose_name='ID Póliza')

    class Meta:
        managed = False
        db_table = 'siniestro'
        verbose_name_plural = 'Siniestros'

    def __str__(self):
        return self.nro_siniestro


class Taller(models.Model):
    id_taller = models.IntegerField(primary_key=True, verbose_name='ID Taller')
    nombre = models.CharField(max_length=30, verbose_name='Nombre Taller')
    razon_social = models.CharField(max_length=50, verbose_name='Razón Social')
    telefono = models.BigIntegerField(verbose_name='Teléfono')
    correo = models.CharField(max_length=30, verbose_name='Correo')
    capacidad_taller = models.IntegerField(verbose_name='Capacidad Taller')
    estado = models.CharField(max_length=1, verbose_name='Estado')
    estado_delete = models.CharField(max_length=1)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario')

    class Meta:
        managed = False
        db_table = 'taller'
        verbose_name_plural = 'Talleres'

    def __str__(self):
        return self.nombre


class TipoAccidente(models.Model):
    id_tipo_acc = models.IntegerField(
        primary_key=True, verbose_name='ID Tipo Accidente')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    class Meta:
        managed = False
        db_table = 'tipo_accidente'
        verbose_name_plural = 'Tipo Accidentes'

    def __str__(self):
        return self.nombre


class TipoActa(models.Model):
    id_tipo_acta = models.FloatField(
        primary_key=True, verbose_name='ID Tipo Acta')
    nombre = models.CharField(max_length=40, verbose_name='Nombre')

    class Meta:
        managed = False
        db_table = 'tipo_acta'
        verbose_name_plural = 'Tipo Actas'

    def __str__(self):
        return self.nombre


class TipoDano(models.Model):
    id_tipo_dano = models.IntegerField(
        primary_key=True, verbose_name='ID Tipo Daño')
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')

    class Meta:
        managed = False
        db_table = 'tipo_dano'
        verbose_name_plural = 'Tipo Daños'

    def __str__(self):
        return self.nombre


class TipoPlan(models.Model):
    id_tip_plan = models.IntegerField(
        primary_key=True, verbose_name='ID Tipo Plan')
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')
    valor = models.IntegerField(verbose_name='Valor')
    cobertura_max = models.IntegerField(verbose_name='Cobertura Máxima')

    class Meta:
        managed = False
        db_table = 'tipo_plan'
        verbose_name_plural = 'Tipo Planes'

    def __str__(self):
        return str(self.id_tip_plan) + ' ' + ' ' + self.nombre + ' ' + str(self.valor)


class TipoVehiculo(models.Model):
    id_tipo_auto = models.IntegerField(
        primary_key=True, verbose_name='ID Tipo Auto')
    tipo = models.CharField(max_length=20, verbose_name='Tipo')

    class Meta:
        managed = False
        db_table = 'tipo_vehiculo'
        verbose_name_plural = 'Tipo Vehículo'

    def __str__(self):
        return self.tipo


class Usuario(models.Model):
    rut_usuario = models.CharField(
        primary_key=True, max_length=12, verbose_name='Rut Usuario')
    primer_nombre = models.CharField(
        max_length=20, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(
        max_length=20, verbose_name='Segundo Nombre')
    primer_apellido = models.CharField(
        max_length=20, verbose_name='Apellido Paterno')
    segundo_apellido = models.CharField(
        max_length=20, verbose_name='Apellido Materno')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    telefono = models.BigIntegerField(verbose_name='Teléfono')
    rol_id_rol = models.ForeignKey(
        Rol, models.DO_NOTHING, db_column='rol_id_rol', verbose_name='ID Rol')

    class Meta:
        managed = False
        db_table = 'usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.rut_usuario


class Vehiculo(models.Model):
    patente_vehiculo = models.CharField(
        primary_key=True, max_length=8, verbose_name='Patente')
    anio = models.IntegerField(verbose_name='Año')
    modelo = models.CharField(max_length=200, verbose_name='Modelo')
    nro_motor = models.CharField(max_length=100, verbose_name='N° Motor')
    tipo_vehiculo_id_tipo_auto = models.ForeignKey(
        TipoVehiculo, models.DO_NOTHING, db_column='tipo_vehiculo_id_tipo_auto', verbose_name='Tipo Vehículo')
    marca_id_marca = models.ForeignKey(
        Marca, models.DO_NOTHING, db_column='marca_id_marca', verbose_name='ID Marca')
    asegurado_rut_asegurado = models.ForeignKey(
        Asegurado, models.DO_NOTHING, db_column='asegurado_rut_asegurado', verbose_name='Rut Asegurado')

    class Meta:
        managed = False
        db_table = 'vehiculo'
        verbose_name_plural = 'Vehículos'

    def __str__(self):
        return self.patente_vehiculo
