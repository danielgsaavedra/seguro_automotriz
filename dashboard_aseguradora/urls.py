from django.urls import path
from .views import DashboardAsegView

urlpatterns = [
    
    path('dashboard/', DashboardAsegView.as_view(), name='dashboard'),
  
]