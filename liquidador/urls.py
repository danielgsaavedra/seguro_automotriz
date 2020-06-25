from django.urls import path
from . import views

urlpatterns = [
    path('siniestros/', views.SiniestroView, name='siniestros_liquidador'),
    path('presupuestos/', views.PresupuestoView, name='presupuestos_liquidador'),
    path('siniestros/disabled', views.SiniestroDisabledView, name='siniestros_disabled_liquidador'),
    path('presupuestos/aprobados', views.PresupuestoAprobadoView, name='presupuestos_aprobados'),
    path('presupuestos/rechazados', views.PresupuestoRechazadoView, name='presupuestos_rechazados'),
    path('reportes/', views.ReportesView, name='reportes'),
]
