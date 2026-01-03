from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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
        
        
class CustomLoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email',
            'class': 'input-field'
        })
    )
    password= forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "input-field",
            "placeholder": "Enter password"
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        if email and password:
            user = authenticate(username=email,password=password)
            if user is None:
                raise forms.ValidationError("Invalid email or password")
            self.user = user
        return cleaned_data