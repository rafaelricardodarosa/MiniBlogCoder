<<<<<<< HEAD
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]
        help_texts = {k:"" for k in fields }
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ["first_name", "last_name",  "email", "password1", "password2"]
        help_texts = {k:"" for k in fields }
        
        
class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    class Meta:
        model = User
        fields = ["first_name", "last_name",  "email", "password1", "password2"]
        help_texts = {k:"" for k in fields }
=======
from django.forms import ModelForm

from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
>>>>>>> 2a1b38b098010972325ce498d1608cc0cf625009
