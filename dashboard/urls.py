
from django.urls import path
from django.conf.urls import url, include
from .views import DashboardView, SiniestrosView, UsuariosView, TallerView
from . import views

urlpatterns = [

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('siniestros/', SiniestrosView.as_view(), name='siniestros'),
    path('taller/', views.TallerView, name='taller'),
    path('usuarios/', views.UsuariosView, name='usuarios'),
    path('asegurados/', views.AseguradosView, name='asegurados'),
    path('vehiculos/', views.VehiculosView, name='vehiculos'),
    url(r'^polizas/$', views.PolizasView, name='polizas'),
    url(r'^polizas/create$', views.CreatePoliza, name='poliza_create'),
    # update
    # delete
]
