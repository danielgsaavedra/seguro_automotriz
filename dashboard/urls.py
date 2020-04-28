  
from django.urls import path
from .views import DashboardView, SiniestrosView
from . import views
urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('siniestros/', SiniestrosView.as_view(), name='siniestros'),
    path('asegurados/', views.AseguradosView, name='asegurados'),
    path('vehiculos/', views.VehiculosView, name='vehiculos'),
    path('polizas/', views.PolizasView, name='polizas'),
  
]