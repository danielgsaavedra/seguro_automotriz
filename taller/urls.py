from django.urls import path
from . import views
from .views import SiniestrosRecepcionView, SiniestrosRetiroView, InformeDañosView, PresupuestoView, ActaRecepcionView

urlpatterns = [
    path('siniestro_recepcion/', views.SiniestrosRecepcionView, name='siniestro_recepcion'),
    path('acta_recepcion/create', views.CreateActaRecepcion, name='acta_recepcion_create'),
    path('acta_recepcion/', views.ActaRecepcionView, name='acta_recepcion'),
    path('siniestro_retiro/', views.SiniestrosRetiroView, name='siniestro_retiro'),
    path('acta_retiro/create', views.CreateActaRetiro, name='acta_retiro_create'),
    path('acta_retiro/', views.ActaRetiroView, name='acta_retiro'),
    path('acta_rechazo/create', views.CreateActaRechazo, name='acta_rechazo_create'),
    path('informe_daños/', views.InformeDañosView, name='informe_daños'),
    path('acta_rechazo/', views.ActaRechazoView, name='acta_rechazo'),
    path('presupuesto/', views.PresupuestoView, name='presupuesto'),
]
