from django.contrib import admin
from .models import Asegurado,Comuna,Region,Taller,Siniestro,Vehiculo,Poliza,Marca,TipoVehiculo,Usuario,Rol,TipoAccidente,Direccion

admin.site.register(Asegurado)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(Taller)
admin.site.register(Siniestro)
admin.site.register(Vehiculo)
admin.site.register(Poliza)
admin.site.register(Marca)
admin.site.register(TipoVehiculo)
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(TipoAccidente)
admin.site.register(Direccion)