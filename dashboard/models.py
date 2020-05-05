from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.


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
    telefono = models.IntegerField(verbose_name='Teléfono')
    fecha_nacimiento = models.DateField(verbose_name='Fecha Nacimiento')
    estado = models.CharField(max_length=1, default=1)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'asegurado'
    #     verbose_name_plural = 'Asegurados'

    def __str__(self):
        return self.rut_asegurado


class Comuna(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    region_nro_region = models.ForeignKey(
        'Region', models.DO_NOTHING, db_column='region_nro_region', verbose_name='Región', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'comuna'
    #     verbose_name_plural = 'Comuna'

    def __str__(self):
        return self.nombre


class Direccion(models.Model):
    calle = models.CharField(max_length=50, verbose_name='Calle')
    numero = models.IntegerField(verbose_name='N°')
    comuna_id_comuna = models.ForeignKey(
        'Comuna', models.DO_NOTHING, db_column='comuna_id_comuna', verbose_name='Comuna', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', blank=True, null=True, verbose_name='Rut Usuario')
    asegurado_rut_asegurado = models.ForeignKey(
        'Asegurado', models.DO_NOTHING, db_column='asegurado_rut_asegurado', blank=True, null=True, verbose_name='Asegurado')
    servicio_grua_id_servicio = models.ForeignKey(
        'ServicioGrua', models.DO_NOTHING, db_column='servicio_grua_id_servicio', blank=True, null=True, verbose_name='Servicio GRúa')
    siniestro_id = models.ForeignKey(
        'Siniestro', models.DO_NOTHING, db_column='siniestro_id', blank=True, null=True, verbose_name='ID Siniestro')
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', blank=True, null=True, verbose_name='Taller')

    # class Meta:
    #     managed = False
    #     db_table = 'direccion'
    #     verbose_name_plural = 'Direcciones'

    def __str__(self):
        return self.calle + ' ' + '#' + str(self.numero)


class EstadoPresupuesto(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')

    # class Meta:
    #     managed = False
    #     db_table = 'estado_presupuesto'
    #     verbose_name_plural = 'Estado Presupuestos'

    def __str__(self):
        return self.nombre


class EstadoSiniestro(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')

    # class Meta:
    #     managed = False
    #     db_table = 'estado_siniestro'
    #     verbose_name_plural = 'Estado Siniestros'

    def __str__(self):
        return str(self.nombre)


class FormularioActa(models.Model):
    fecha_hora = models.DateField(verbose_name='Fecha')
    observaciones = models.CharField(
        max_length=300, blank=True, null=True, verbose_name='Observaciones')
    tipo_acta_id_tipo_acta = models.ForeignKey(
        'TipoActa', models.DO_NOTHING, db_column='tipo_acta_id_tipo_acta', verbose_name='Tipo Acta', null=True)
    siniestro_id = models.ForeignKey(
        'Siniestro', models.DO_NOTHING, db_column='siniestro_id', verbose_name='ID Siniestro', null=True)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'formulario_acta'
    #     verbose_name_plural = 'Formulario Actas'

    # def __str__(self):
    #     return str(self.fecha_hora)


class Grua(models.Model):
    patente_grua = models.CharField(
        primary_key=True, max_length=10, verbose_name='Patente Grúa')
    estado = models.CharField(max_length=1, verbose_name='Estado')
    servicio_grua_id_servicio = models.ForeignKey(
        'ServicioGrua', models.DO_NOTHING, db_column='servicio_grua_id_servicio', verbose_name='Servicio Grúa', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'grua'
    #     verbose_name_plural = 'Grúas'

    def __str__(self):
        return self.patente_grua


class InformeDano(models.Model):
    fecha_hora = models.DateField(verbose_name='Fecha')
    observaciones = models.CharField(
        max_length=500, verbose_name='Observaciones')
    perdida_total = models.CharField(
        max_length=1, blank=True, null=True, verbose_name='Perdida Total')
    tipo_dano_id_tipo_dano = models.ForeignKey(
        'TipoDano', models.DO_NOTHING, db_column='tipo_dano_id_tipo_dano', verbose_name='Tipo Daño', null=True)
    severidad_dano_id_seve_dano = models.ForeignKey(
        'SeveridadDano', models.DO_NOTHING, db_column='severidad_dano_id_seve_dano', verbose_name='Severidad Daño', null=True)
    vehiculo_patente_vehiculo = models.ForeignKey(
        'Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente_vehiculo', verbose_name='Patente Vehículo', null=True)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', null=True)
    siniestro_id = models.ForeignKey(
        'Siniestro', models.DO_NOTHING, db_column='siniestro_id', verbose_name='ID Siniestro', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'informe_dano'
    #     verbose_name_plural = 'Informe Daños'

    # def __str__(self):
    #     return str(self.id_info_dano)


class Marca(models.Model):
    nombre = models.CharField(max_length=20, verbose_name='Nombre Marca')

    # class Meta:
    #     managed = False
    #     db_table = 'marca'

    def __str__(self):
        return str(self.nombre)


class PlanSeguro(models.Model):
    tipo_plan_id_tip_plan = models.ForeignKey(
        'TipoPlan', models.DO_NOTHING, db_column='tipo_plan_id_tip_plan', verbose_name='Tipo Plan', null=True)
    poliza_id_poliza = models.ForeignKey(
        'Poliza', models.DO_NOTHING, db_column='poliza_id_poliza', verbose_name='ID Póliza', null=True)
    deducible = models.IntegerField(verbose_name='Deducible')

    # class Meta:
    #     managed = False
    #     db_table = 'plan_seguro'
    #     unique_together = (('tipo_plan_id_tip_plan', 'poliza_id_poliza'),)
    #     verbose_name_plural = 'Plan Seguros'

    # def __str__(self):
    #     return str(self.tipo_plan_id_tip_plan)


class Poliza(models.Model):
    vigente = models.CharField(
        max_length=1, verbose_name='Vigencia', default=1)
    fecha_inicio = models.DateField(verbose_name='Fecha Inicio')
    fecha_fin = models.DateField(verbose_name='Fecha Termino')
    estado = models.CharField(max_length=1, default=1)
    asegurado_rut_asegurado = models.ForeignKey(
        'Asegurado', models.DO_NOTHING, db_column='asegurado_rut_asegurado', verbose_name='Rut Asegurado', null=True)
    vehiculo_patente_vehiculo = models.ForeignKey(
        'Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente_vehiculo', verbose_name='Patente Vehículo', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'poliza'
    #     verbose_name_plural = 'Pólizas'

    def __str__(self):
        return str(self.id)


class Presupuesto(models.Model):
    fecha_hora = models.DateField(verbose_name='Fecha')
    valor_total = models.IntegerField(verbose_name='Valor Total')
    estado_id_est_presupuesto = models.ForeignKey(
        'EstadoPresupuesto', models.DO_NOTHING, db_column='estado_id_est_presupuesto', verbose_name='ID Est. Presupuesto', null=True)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', blank=True, null=True, verbose_name='Rut Usuario')
    informe_dano_id_info_dano = models.ForeignKey(
        'InformeDano', models.DO_NOTHING, db_column='informe_dano_id_info_dano', verbose_name='ID Inf. Daño', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'presupuesto'
    #     verbose_name_plural = 'Presupuestos'

    # def __str__(self):
    #     return str(self.id_presupuesto) + ' ' + str(self.valor_total)


class RegAsegurado(models.Model):
    nombre_registrador = models.CharField(max_length=30)
    nombre_asegurado = models.CharField(max_length=30)
    nro_poliza = models.IntegerField()
    fecha_hora = models.DateField()

    # class Meta:
    #     managed = False
    #     db_table = 'reg_asegurado'


class RegError(models.Model):
    error = models.CharField(max_length=50)
    cod_error = models.CharField(max_length=500)
    mensaje = models.CharField(max_length=300)
    fecha_hora = models.DateField()

    # class Meta:
    #     managed = False
    #     db_table = 'reg_error'


class RegGrua(models.Model):
    nombre_registrador = models.CharField(max_length=30)
    patente_grua = models.CharField(max_length=7)
    fecha_hora = models.DateField()

    # class Meta:
    #     managed = False
    #     db_table = 'reg_grua'


class RegPoliza(models.Model):
    nombre_registrador = models.CharField(max_length=30)
    nro_poliza = models.IntegerField()
    fecha_hora = models.DateField()

    # class Meta:
    #     managed = False
    #     db_table = 'reg_poliza'


class RegSiniestro(models.Model):
    nombre_registrador = models.CharField(max_length=30)
    id_siniestro = models.IntegerField()
    fecha_hora = models.DateField()

    # class Meta:
    #     managed = False
    #     db_table = 'reg_siniestro'


class RegTaller(models.Model):
    nombre_registrador = models.CharField(max_length=30)
    nombre_taller = models.CharField(max_length=30)
    fecha_hora = models.DateField()

    # class Meta:
    #     managed = False
    #     db_table = 'reg_taller'


class RegUsuario(models.Model):
    nombre_registrador = models.CharField(max_length=30)
    nombre_registrado = models.CharField(max_length=30)
    fecha_hora = models.DateField()

    # class Meta:
    #     managed = False
    #     db_table = 'reg_usuario'


class Region(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre Región')

    # class Meta:
    #     managed = False
    #     db_table = 'region'
    #     verbose_name_plural = 'Regiones'

    def __str__(self):
        return self.nombre


class ServicioGrua(models.Model):
    nombre = models.CharField(max_length=400, verbose_name='Nombre')
    razon_social = models.CharField(max_length=50, verbose_name='Razón Social')
    telefono = models.BigIntegerField(verbose_name='Teléfono')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'servicio_grua'
    #     verbose_name_plural = 'Servicios Grúas'

    def __str__(self):
        return self.nombre


class SeveridadDano(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre ')

    # class Meta:
    #     managed = False
    #     db_table = 'severidad_dano'
    #     verbose_name_plural = 'Severidad Daños'

    def __str__(self):
        return self.nombre


class Siniestro(models.Model):
    fecha_hr = models.DateField(verbose_name='Fecha Siniestro')
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')
    parte_policial = models.FileField(
        max_length=100, blank=True, null=True, verbose_name='Parte Policial')
    foto_licencia = models.FileField(
        max_length=100, blank=True, null=True, verbose_name='Foto Licencia')
    tipo_accidente_id_tipo_acc = models.ForeignKey(
        'TipoAccidente', models.DO_NOTHING, db_column='tipo_accidente_id_tipo_acc', verbose_name='Tipo Accidente', null=True)
    est_siniestro_id_est_siniestro = models.ForeignKey(
        'EstadoSiniestro', models.DO_NOTHING, db_column='est_siniestro_id_est_siniestro', verbose_name='Estado Siniestro', default=1, null=True)
    taller_id_taller = models.ForeignKey(
        'Taller', models.DO_NOTHING, db_column='taller_id_taller', verbose_name='Taller', null=True)
    grua_patente_grua = models.ForeignKey(
        'Grua', models.DO_NOTHING, db_column='grua_patente_grua', blank=True, null=True, verbose_name='Patente Grúa')
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)
    poliza_id_poliza = models.ForeignKey(
        'Poliza', models.DO_NOTHING, db_column='poliza_id_poliza', verbose_name='ID Póliza', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'siniestro'
    #     verbose_name_plural = 'Siniestros'

    def __str__(self):
        return str(self.id)


class Taller(models.Model):
    nombre = models.CharField(max_length=30, verbose_name='Nombre Taller')
    razon_social = models.CharField(max_length=50, verbose_name='Razón Social')
    telefono = models.IntegerField(verbose_name='Teléfono')
    correo = models.CharField(max_length=30, verbose_name='Correo')
    capacidad_taller = models.IntegerField(verbose_name='Capacidad Taller')
    estado = models.CharField(max_length=1, verbose_name='Estado', default=1)
    estado_delete = models.CharField(max_length=1, default=1)
    usuario_rut_usuario = models.ForeignKey(
        'Usuario', models.DO_NOTHING, db_column='usuario_rut_usuario', verbose_name='Rut Usuario', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'taller'
    #     verbose_name_plural = 'Talleres'

    def __str__(self):
        return self.nombre


class TipoAccidente(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_accidente'
    #     verbose_name_plural = 'Tipo Accidentes'

    def __str__(self):
        return self.nombre


class TipoActa(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre')

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_acta'
    #     verbose_name_plural = 'Tipo Actas'

    def __str__(self):
        return self.nombre


class TipoDano(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_dano'
    #     verbose_name_plural = 'Tipo Daños'

    def __str__(self):
        return self.nombre


class TipoPlan(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Nombre')
    descripcion = models.CharField(max_length=500, verbose_name='Descripción')
    valor = models.IntegerField(verbose_name='Valor')
    cobertura_max = models.IntegerField(verbose_name='Cobertura Máxima')

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_plan'
    #     verbose_name_plural = 'Tipo Planes'

    # def __str__(self):
    #     return str(self.id_tip_plan) + ' ' + ' ' + self.nombre + ' ' + str(self.valor)


class TipoVehiculo(models.Model):
    tipo = models.CharField(max_length=20, verbose_name='Tipo')

    # class Meta:
    #     managed = False
    #     db_table = 'tipo_vehiculo'
    #     verbose_name_plural = 'Tipo Vehículo'

    def __str__(self):
        return self.tipo

class UsuarioManager(BaseUserManager):
    def create_user(self,email,rut_usuario,primer_nombre,primer_apellido,password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo')

        usuario = self.model(
            rut_usuario = rut_usuario,
            email = self.normalize_email(email),
            primer_nombre = primer_nombre,
            primer_apellido=primer_apellido
        )
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,email,rut_usuario,primer_nombre,primer_apellido,password):
        usuario = self.create_user(
            email,
            rut_usuario = rut_usuario,
            primer_nombre = primer_nombre,
            primer_apellido=primer_apellido,
            password=password
        )
        usuario.is_administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    
    opciones = [
        ("1", 'Mesa de Ayuda'),
        ("2", 'Liquidador'),
        ("3", 'Personal Taller'),
        ("4", 'Personal Grua'),
    ]

    rut_usuario = models.CharField(unique=True, max_length=12, verbose_name='Rut Usuario')
    primer_nombre = models.CharField(max_length=20, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=20, verbose_name='Segundo Nombre',null=True)
    primer_apellido = models.CharField(max_length=20, verbose_name='Apellido Paterno')
    segundo_apellido = models.CharField(max_length=20, verbose_name='Apellido Materno',null=True)
    email = models.EmailField(max_length=254, verbose_name='Correo',unique=True)
    telefono = models.BigIntegerField(verbose_name='Teléfono',null=True)
    rol = models.CharField(max_length=30,choices=opciones,null=True)
    is_active = models.BooleanField(default=True)
    is_administrador = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'rut_usuario'
    REQUIRED_FIELDS = ['email','primer_nombre','primer_apellido']

    # class Meta:
    #     managed = False
    #     db_table = 'usuario'
    #     verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.rut_usuario
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_administrador
    

class Vehiculo(models.Model):
    patente_vehiculo = models.CharField(
        primary_key=True, max_length=8, verbose_name='Patente')
    anio = models.IntegerField(verbose_name='Año')
    modelo = models.CharField(max_length=200, verbose_name='Modelo')
    nro_motor = models.CharField(max_length=100, verbose_name='N° Motor')
    tipo_vehiculo_id_tipo_auto = models.ForeignKey(
        'TipoVehiculo', models.DO_NOTHING, db_column='tipo_vehiculo_id_tipo_auto', verbose_name='Tipo Vehículo', null=True)
    marca_id_marca = models.ForeignKey(
        'Marca', models.DO_NOTHING, db_column='marca_id_marca', verbose_name='ID Marca', null=True)
    asegurado_rut_asegurado = models.ForeignKey(
        'Asegurado', models.DO_NOTHING, db_column='asegurado_rut_asegurado', verbose_name='Rut Asegurado', null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'vehiculo'
    #     verbose_name_plural = 'Vehículos'

    def __str__(self):
        return self.patente_vehiculo
