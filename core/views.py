from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from .models import User

def register(request):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print('INSIDE FORM')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    user = request.user
    if user.role == 'student':
        return render(request, 'dashboard.html')
    elif user.role == 'staff':
        return render(request, 'dashboard.html')
    elif user.role == 'admin':
        return render(request, 'dashboard.html')
    elif user.role == 'editor':
        return render(request, 'dashboard.html')
    else:
        return redirect('login')
