from django.shortcuts import render, redirect
from .forms import AdminRegistrationForm
from accounts.models import UserProfile, User
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.forms import AdminRegistrationForm

from .forms import UserProfileForm

@login_required
def perfil_usuario(request):
    user = request.user
    profile = user.userprofile
    

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
           
            form.save()
            return redirect('perfil_usuario')

    else:
        try:
            profile = user.userprofile
            form = UserProfileForm(instance=user)
        except UserProfile.DoesNotExist:
            profile = None
            form = UserProfileForm()
    

    return render(request, 'pages/perfil_usuario.html', {'user': user, 'profile': profile, 'form': form})

def editar_perfil(request):
    user = request.user
    profile = user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('accounts:perfil_usuario')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'pages/editar_perfil.html', {'form': form})

def admin_registration(request):
    if request.method == 'POST':
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:dashboard')
    else:
        form = AdminRegistrationForm()
    
    return render(request, 'pages/vista_admin.html', {'form': form})



def dashboard_admin(request):    
    return render(request, 'pages/dashboard.html')
#CRUD USUARIOS
def actualizar(request):  
    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('password1') and request.POST.get('password2') and request.POST.get('bio') and request.POST.get('avatar') and request.POST.get('rol_cs'):
            user = User()
            user.id = request.POST.get('id')
            user.username = request.POST.get('nombre')
            user.password1 = request.POST.get('password1')
            user.password2 = request.POST.get('password2')
            user.bio = request.POST.get('bio')
            user.avatar = request.POST.get('avatar')
            user.rol_cs = request.POST.get('rol_cs')
            user.save()
            return redirect('users:actualizar')
    else:
        users = User.objects.all()
        datos = {'usuarios': users } 
        return render(request, 'crud_usuarios/actualizar.html', datos)

def agregar(request):    
    if request.method=='POST':
        if request.POST.get('username') and request.POST.get('password1') and request.POST.get('password2') and request.POST.get('bio') and request.POST.get('avatar') and request.POST.get('rol_cs'):
            user = User()
            user.username = request.POST.get('nombre')
            user.password1 = request.POST.get('password1')
            user.password2 = request.POST.get('password2')
            user.bio = request.POST.get('bio')
            user.avatar = request.POST.get('avatar')
            user.rol_cs = request.POST.get('rol_cs')
            user.save()
            return redirect('users:actualizar')
    else:
        return render(request, 'crud_usuarios/agregar.html')
            

    return render(request, 'crud_usuarios/agregar.html')
def eliminar(request):   
    if request.method=='POST':
        if request.POST.get('id'):
            id_a_borrar =  request.POST.get('id')
            tupla = User.objects.get(id= id_a_borrar)
            tupla.delete()
            return redirect('users:listar')
    else:
        users = User.objects.all()
        datos = {'usuarios': users } 
        return render(request, 'crud_usuarios/eliminar.html', datos)
def listar(request):    
    users = User.objects.all()
    datos = {'usuarios': users }
    return render(request, 'crud_usuarios/listar.html', datos)


    
        

