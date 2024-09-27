from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ICSUrlForm(forms.Form):
    ics_url = forms.URLField(label='ICS fájl URL', max_length=255)

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']