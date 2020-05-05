from django.urls import path
from django.conf.urls import url, include
from .views import DashboardView, TallerView
from . import views

urlpatterns = [

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('siniestros/', views.SiniestroView, name='siniestros'),
    path('siniestros/create', views.CreateSiniestro, name='siniestro_create'),
    path('siniestros/<str:id>/update',
         views.UpdateSiniestro, name='siniestro_update'),
    path('siniestros/<str:id>/delete',
         views.DeleteSiniestro, name='siniestro_delete'),
    path('siniestros/disabled', views.SiniestroDisabledView, name='siniestro_disabled'),
    path('taller/', views.TallerView, name='taller'),
    path('taller/create/', views.CreateTaller, name='taller_create'),
    path('taller/<str:id>/update', views.UpdateTaller, name='taller_update'),
    path('taller/<str:id>/delete', views.DeleteTaller, name='taller_delete'),
    path('taller/<str:id>/reactivate', views.ReactivateTaller, name='taller_reactivate'),
    path('taller/disabled', views.TallerDisabledView, name='taller_disabled'),
    path('asegurados/', views.AseguradosView, name='asegurados'),
    path('asegurados/disabled', views.AseguradosDisableView, name='asegurados_disabled'),
    path('asegurados/create/', views.AseguradoCreate, name='asegurado_create'),
    path('asegurados/<str:id>/update/',
         views.AseguradoUpdate, name='asegurado_update'),
    path('asegurados/<str:id>/delete/',
         views.AseguradoDelete, name='asegurado_delete'),
    path('asegurados/<str:id>/reactivate', views.ReactivateAsegurado, name='asegurado_reactivate'),
    path('vehiculos/', views.VehiculosView, name='vehiculos'),
    path('vehiculos/create/', views.VehiculoCreate, name='vehiculo_create'),
    path('vehiculos/<str:id>/update/',
         views.VehiculoUpdate, name='vehiculo_update'),
    path('polizas/disabled', views.PolizasDisableView, name='poliza_disabled'),
    path('polizas/', views.PolizasView, name='polizas'),
    path('polizas/create', views.CreatePoliza, name='poliza_create'),
    path('polizas/<str:id>/update', views.UpdatePoliza, name='poliza_update'),
    path('polizas/<str:id>/delete', views.DeletePoliza, name='poliza_delete'),
    path('polizas/<str:id>/reactivate', views.ReactivatePoliza, name='poliza_reactivate'),
]
