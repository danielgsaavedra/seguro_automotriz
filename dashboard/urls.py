  
from django.urls import path
from .views import DashboardView, ListarSiniestrosView

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
     path('listar-siniestros/', ListarSiniestrosView.as_view(), name='listar-siniestros'),
  
]