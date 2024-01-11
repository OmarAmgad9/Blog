from django.forms import ModelForm, TextInput
from .models import Rooms, Messeag
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = ['topic', 'name', 'descriptions']
        # fields = "__all__"
        

class MessageForm(ModelForm):
    class Meta:
        model = Messeag
        fields = ['body'] #, 'room']
        # fields = "__all__"
    body=forms.CharField(widget=forms.Textarea(attrs={
        "class": 'text-dark',
    }))

class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'text-dark form-control',
        'placeholder': 'Enter Your Name',
        'style': 'margin-bottom:10px;'
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'text-dark form-control',
        'placeholder': 'Enter Your Email',
        'style': 'margin-bottom:10px;'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'text-dark form-control',
        'placeholder': 'Enter Strong Password',
        'style': 'margin-bottom:10px;'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'text-dark form-control',
        'placeholder': 'Confirme Password',
        'style': 'margin-bottom:10px;'
    }))
