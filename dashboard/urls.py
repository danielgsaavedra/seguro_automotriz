  
from django.urls import path
from .views import DashboardView, SiniestrosView, UsuariosView
from . import views

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('siniestros/', SiniestrosView.as_view(), name='siniestros'),
    path('usuarios/', views.UsuariosView, name='usuarios'),
  
]