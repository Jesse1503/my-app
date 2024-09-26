from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm 
from django.contrib.auth.views import LoginView 
from django.contrib.auth import authenticate, login, logout 

 
# Create your views here.
def cart(request):
 return   render(request,'ecom/cart.html')

def checkout(request):
 return   render(request, 'ecom/checkout.html' )

def store(request):
    return  render(request,'ecom/store.html')

def login_page(request):
     if request.method == 'POST':

        username = request.POST.get('username')
        password =  request.POST.get('password')

        user = authenticate(username=username,password=password)


        if user is not None:

            login(request, user)


     
     
     
     
     
     
     
     return render(request,'ecom/login.html') 
            
def signup(request):
    form = CustomUserCreationForm ()
    if request.method == 'POST':
       
        form = CustomUserCreationForm (request.POST)
        
        if form.is_valid():
            
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Form submitted successfully ' + user)
            return redirect('login')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors.')
    context = {
           'form': form

        }
 
    return  render(request,'ecom/signup.html',context)






























