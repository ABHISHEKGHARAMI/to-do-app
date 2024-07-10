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
    
    return register(request,
                    'register.html',
                    {
                        'form':form
                    }) 