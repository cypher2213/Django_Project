from django.shortcuts import render, redirect
from products.models import Product
from reviews import forms
from core.forms import CustomRegisterForm, CustomLoginForm
from django.contrib.auth import login,logout
# Create your views here.

def home(request):
    form = forms.CreateReview(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = forms.CreateReview()
        
    products = Product.objects.all()
    return render(request, 'home.html', {"products":products, 'review_form':form})


def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            login(request,form.user)
            return redirect('home')
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = CustomLoginForm()
    return render(request,'login.html', {"form":form})

def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = CustomRegisterForm()
        
    return render(request,'register.html', {"form":form})

def logout_view(request):
    logout(request)
    return redirect('home')
    