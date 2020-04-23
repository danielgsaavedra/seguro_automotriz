from django.urls import path
from .views import ListarSiniestrosView, DashboardView

urlpatterns = [
    
    path('listar-siniestros/', ListarSiniestrosView.as_view(), name='listar-siniestros'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
  
]