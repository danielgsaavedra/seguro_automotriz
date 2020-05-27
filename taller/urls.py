from django.urls import path
from . import views
from .views import ActaRecepcionView, ActaRetiroView, InformeDañosView, PresupuestoView

urlpatterns = [
    path('acta_recepcion/', views.ActaRecepcionView, name='acta_recepcion'),
    path('acta_retiro/', views.ActaRetiroView, name='acta_retiro'),
    path('informe_daños/', views.InformeDañosView, name='informe_daños'),
    path('presupuesto/', views.PresupuestoView, name='presupuesto'),
]
