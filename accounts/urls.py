from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('perfil_usuario', views.perfil_usuario, name='perfil_usuario'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    
]