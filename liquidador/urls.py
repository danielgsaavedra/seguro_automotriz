from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path('siniestros/', views.SiniestroView, name='siniestros_liquidador'),
    path('siniestros/disabled/', views.SiniestroDisabledView, name='siniestros_disabled_liquidador'),
    path('siniestros/rechazados/', views.SiniestroRechazadosView, name='siniestros_rechazados_liquidador'),
    path('siniestros/pendientes/', views.SiniestroPendientesView, name='siniestros_pendientes_liquidador'),
    path('presupuestos/', views.PresupuestoView, name='presupuestos_liquidador'),
    path('presupuestos/aprobados/', views.PresupuestoAprobadoView, name='presupuestos_aprobados'),
    path('presupuestos/rechazados/', views.PresupuestoRechazadoView, name='presupuestos_rechazados'),
    path('presupuesto/<str:id>/apro_recha/', views.PresupuestoAproRechView, name='presupuesto_apro_recha'),
    path('presupuesto/<str:id>/aprobar/', views.AprobarPresupuesto, name='aprobar_presupuesto'),
    path('presupuesto/<str:id>/rechazar/', views.RechazarPresupuesto, name='rechazar_presupuesto'),
    path('reportes/', views.ReportesView, name='reportes'),
    path('tipos_plan/', views.TipoPlanView, name='tipos_plan'),
    path('tipos_plan/inactivos/', views.TipoPlanInactivos, name='tipos_plan_inactivo'),
    path('tipos_plan/create/', views.TipoPlanCreate, name='tipos_plan_create'),
    path('tipos_plan/<str:id>/update/', views.TipoPlanUpdate, name='tipos_plan_update'),
    path('tipos_plan/<str:id>/delete/', views.TipoPlanDelete, name='tipos_plan_delete'),
    path('tipos_plan/<str:id>/reactive/', views.TipoPlanReactive, name='tipos_plan_reactive'),
    url(r'^PolizaViewPdf/(?P<pk>[0-9]+)/$',
        views.PolizaViewPdf, name='PolizaViewPdf'),
    url(r'^PolizaPdf/(?P<pk>[0-9]+)/$',
        views.PolizaPdf, name='PolizaPdf'),

]
