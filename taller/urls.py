from django.urls import path
from . import views
from django.conf.urls import include, url
from .views import SiniestrosRecepcionView, SiniestrosRetiroView, InformeDañosView, PresupuestoView, ActaRecepcionView

urlpatterns = [
    path('siniestro_recepcion/', views.SiniestrosRecepcionView,
         name='siniestro_recepcion'),
    path('acta_recepcion/<str:id>/create',
         views.CreateActaRecepcion, name='acta_recepcion_create'),
    path('acta_recepcion/', views.ActaRecepcionView, name='acta_recepcion'),
    path('siniestro_retiro/', views.SiniestrosRetiroView, name='siniestro_retiro'),
    path('acta_retiro/<str:id>/create',
         views.CreateActaRetiro, name='acta_retiro_create'),
    path('acta_retiro/', views.ActaRetiroView, name='acta_retiro'),
    path('acta_rechazo/<str:id>/create',
         views.CreateActaRechazo, name='acta_rechazo_create'),
    path('informe_daños/', views.InformeDañosView, name='informe_daños'),
    path('acta_rechazo/', views.ActaRechazoView, name='acta_rechazo'),
    path('presupuesto/', views.PresupuestoView, name='presupuesto'),
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
]
