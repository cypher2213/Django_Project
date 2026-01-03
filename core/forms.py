from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'input-field'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Enter username','class':'input-field'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "input-field",
            "placeholder": "Enter password"
        })
    )
    password2 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "input-field",
            "placeholder": "Enter password"
        })
    )
    

    class Meta:
        model = User
        fields = ['username','email','password1','password2']