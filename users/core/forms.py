from django import forms
from .models import Profile


class profile_update(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = [
            'bio',
            'image',
            'birthdate',
            'city'
        ]