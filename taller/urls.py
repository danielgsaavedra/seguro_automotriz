from django.urls import path
from . import views
from django.conf.urls import include, url
from .views import SiniestrosRecepcionView, SiniestrosRetiroView, SiniestrosInformeDañosView, PresupuestoView, \
    ActaRecepcionView

urlpatterns = [
    path('siniestro/recepcion/', views.SiniestrosRecepcionView,
         name='siniestro_recepcion'),
    path('acta/recepcion/<str:id>/create',
         views.CreateActaRecepcion, name='acta_recepcion_create'),
    path('acta/recepcion/', views.ActaRecepcionView, name='acta_recepcion'),
    path('siniestro/retiro/', views.SiniestrosRetiroView, name='siniestro_retiro'),
    path('acta/retiro/<str:id>/create',
         views.CreateActaRetiro, name='acta_retiro_create'),
    path('acta/retiro/', views.ActaRetiroView, name='acta_retiro'),
    path('acta/rechazo/<str:id>/create',
         views.CreateActaRechazo, name='acta_rechazo_create'),
    path('acta/rechazo/', views.ActaRechazoView, name='acta_rechazo'),
    path('informe/danos/', views.SiniestrosInformeDañosView, name='informe_daños'),
    path('informe/danos/<str:id>/create',
         views.CreateInformeDaños, name='informe_daños_create'),
    path('informe_danos_view/', views.InformeDanosView, name='informe_daños_view'),
    path('presupuesto/', views.PresupuestoView, name='presupuesto'),
    path('siniestros/inspeccionados/',
         views.SiniestrosInpeccionadosView, name='siniestros_inspecc'),
    path('siniestros/<str:id>/inspeccionados',
         views.CambiarEstadoEnReparacion, name='cambiar_estado_reparacion'),
    path('siniestros/enreparacion/', views.SiniestrosEnReparacionView,
         name='siniestros_enreparacion'),
    path('siniestros/<str:id>/enreparacion',
         views.CambiarEstadoReparado, name='cambiar_estado_reparado'),
    url(r'^actaRecepcionViewPdf/(?P<pk>[0-9]+)/$',
        views.actaRecepcionViewPdf, name='actaRecepcionViewPdf'),
    url(r'^actaRecepcionPdf/(?P<pk>[0-9]+)/$',
        views.actaRecepcionPdf, name='actaRecepcionPdf'),
    url(r'^actaRetiroViewPdf/(?P<pk>[0-9]+)/$',
        views.actaRetiroViewPdf, name='actaRetiroViewPdf'),
    url(r'^actaRetiroPdf/(?P<pk>[0-9]+)/$',
        views.actaRetiroPdf, name='actaRetiroPdf'),
    url(r'^actaRechazoViewPdf/(?P<pk>[0-9]+)/$',
        views.actaRechazoViewPdf, name='actaRechazoViewPdf'),
    url(r'^actaRechazoPdf/(?P<pk>[0-9]+)/$',
        views.actaRechazoPdf, name='actaRechazoPdf'),
    url(r'^informeDanoViewPdf/(?P<pk>[0-9]+)/$',
        views.informeDanoViewPdf, name='informeDanoViewPdf'),
    url(r'^informeDanoPdf/(?P<pk>[0-9]+)/$',
        views.informeDanoPdf, name='informeDanoPdf'),
]
