  
from django.urls import path
from .views import DashboardView, SiniestrosView, UsuariosView, TallerView
from . import views

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('siniestros/', SiniestrosView.as_view(), name='siniestros'),
    path('taller/', views.TallerView, name='taller'),
    path('usuarios/', views.UsuariosView, name='usuarios'),
    path('asegurados/', views.AseguradosView, name='asegurados'),
  
]