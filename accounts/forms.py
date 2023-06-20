from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']

        labels = {
            'bio': 'Biografía',
            'avatar': 'Avatar',
        }

        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

