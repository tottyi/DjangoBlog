from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Posts
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class Registracia(ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'body')