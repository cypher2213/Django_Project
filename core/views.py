from django.shortcuts import render, redirect
from products.models import Product
from reviews import forms
from .forms import CustomRegisterForm

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


def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("FORM ERRORS:", form.errors)
    else:
        form = CustomRegisterForm()
        
    return render(request,'register.html', {"form":form})