from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm,TodoForm
from .models import Todo

# Create your views here.

# first registering the user
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('todo_list')
            
    else:
        form = UserCreationForm()
    
    return render(request,
                'register.html',
                    {
                        'form':form
                    }) 
    
    
# login view
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('todo_list')
    else:
        form = AuthenticationForm()
    return render(
        request,
        'login.html',
        {
            'form':form
        }
    )