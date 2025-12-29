from django.shortcuts import render, redirect
from products.models import Product
from reviews import forms

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

def about(request):
    return render(request,'about.html')