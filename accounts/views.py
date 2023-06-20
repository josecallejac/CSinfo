from django.shortcuts import render, redirect

from accounts.models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

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
