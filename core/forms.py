from allauth.account.forms import LoginForm
from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm
User = get_user_model()
from django.contrib.auth.models import Group



class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_staff'] = forms.BooleanField(label='¿Crear cuenta de administrador?', required=False)
       # self.fields['nacionalidad'] = forms.CharField(label='id_nacionalidad', required=True)

    def save(self, request):
        user = super().save(request)
        is_staff = self.cleaned_data.get('is_staff')
        

        if is_staff:
            user.is_staff = True
            user.is_superuser = False
            # Aquí puedes asignar los roles adicionales para los administradores si es necesario
            administrators_group = Group.objects.get(name='Administrador')
            user.groups.add(administrators_group)
        else:
            user.is_staff = False
            user.is_superuser = False

        user.save()
        return user
    
        
    
    

        
    

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'})
        self.fields['login'].label = ''
        self.fields['password'].label = ''


