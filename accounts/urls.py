from django.urls import path
from . import views
from .views import dashboard_admin, admin_registration


app_name = "accounts"

urlpatterns = [
    path('perfil_usuario', views.perfil_usuario, name='perfil_usuario'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('vista_admin', views.admin_registration, name='vista_admin'),
    # path('admin/register/', admin_registration, name='admin_registration'),
    path('dashboard', dashboard_admin, name='dashboard'),
    #crud
    path('actualizar', views.actualizar, name='actualizar'),
    path('listar', views.listar , name='listar'),
    path('agregar', views.agregar, name='agregar'),
    path('eliminar', views.eliminar, name='eliminar'),
  
    
    
    
]