from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username',
            }),
            "first_name": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name',
            }),
            "password1": forms.PasswordInput(attrs={
                'class': 'form-control',
            }),
            "password2": forms.PasswordInput(attrs={
                'class': 'form-control',
            }),

        }
        labels = {
            'username': 'یوزر',
            'first_name': 'نام',
            'email': 'ایمیل',
            'password1': 'پسورد',
            'password2': 'پسورد',
        }