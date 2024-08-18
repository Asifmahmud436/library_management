from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request,'register.html',{'form':form})
    
def profile(request):
    return render(request,'profile.html')
    
def sign_out(request):
    logout(request)
    return redirect('sign_in')
