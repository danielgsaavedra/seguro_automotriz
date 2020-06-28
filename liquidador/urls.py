from django.urls import path
from . import views

urlpatterns = [
    path('siniestros/', views.SiniestroView, name='siniestros_liquidador'),
    path('presupuestos/', views.PresupuestoView, name='presupuestos_liquidador'),
    path('siniestros/disabled/', views.SiniestroDisabledView, name='siniestros_disabled_liquidador'),
    path('presupuestos/aprobados/', views.PresupuestoAprobadoView, name='presupuestos_aprobados'),
    path('presupuestos/rechazados/', views.PresupuestoRechazadoView, name='presupuestos_rechazados'),
    path('reportes/', views.ReportesView, name='reportes'),
    path('tipos_plan/', views.TipoPlanView, name='tipos_plan'),
    path('tipos_plan/inactivos/', views.TipoPlanInactivos, name='tipos_plan_inactivo'),
    path('tipos_plan/create/', views.TipoPlanCreate, name='tipos_plan_create'),
    path('tipos_plan/<str:id>/update/', views.TipoPlanUpdate, name='tipos_plan_update'),
    path('tipos_plan/<str:id>/delete/', views.TipoPlanDelete, name='tipos_plan_delete'),
]
