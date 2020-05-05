from django.urls import path
from .views import LoginPageView, RegisterPageView
from . import views

urlpatterns = [

    path('usuarios/', views.UsuariosView, name='usuarios'),
    path('usuarios/create/', views.UsuarioCreate, name='usuario_create'),
    path('usuarios/<str:id>/update/', views.UsuarioUpdate, name='usuario_update'),
    path('usuarios/<str:id>/delete/', views.UsuarioDelete, name='usuario_delete'),
    path('usuarios/disabled/', views.UsuariosDisableView, name='usuario_disabled'),
    path('usuario/<str:id>/reactivate', views.ReactivateUsuario, name='usuario_reactivate'),

]
