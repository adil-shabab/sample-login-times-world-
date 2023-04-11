from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUsers

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUsers
        fields = ('name', 'email', 'role', 'country', 'nationality', 'mobile', 'password1', 'password2')

