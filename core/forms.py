from allauth.account.forms import LoginForm
from django import forms
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm

from django.contrib.auth.models import Group

from accounts.models import UserProfile




class CustomSignupForm(SignupForm):
    
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'avatar']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
             
    
    

        
    

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Password'})
        self.fields['login'].label = ''
        self.fields['password'].label = ''


