  
from django.urls import path
from .views import DashboardView, SiniestrosView

urlpatterns = [
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
     path('siniestros/', SiniestrosView.as_view(), name='siniestros'),
  
]