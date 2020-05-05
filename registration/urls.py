from django.urls import path
from .views import LoginPageView, RegisterPageView
from . import views
from django.contrib.auth.views import LoginView 

urlpatterns = [

    path('',LoginView.as_view(),{'template_name':'login.html'},name='login'),
    path('registro/', RegisterPageView.as_view(), name='registro'),
    path('usuarios/', views.UsuariosView, name='usuarios'),
    path('usuarios/create/', views.UsuarioCreate, name='usuario_create'),
    path('usuarios/<str:id>/update/',views.UsuarioUpdate, name='usuario_update'),
    path('usuarios/<str:id>/delete/',views.UsuarioDelete, name='usuario_delete'),

]
