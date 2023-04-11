from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm
from .models import CustomUsers

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('working')
        if form.is_valid():
    
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')

            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email,password)
        user = authenticate(request, email=email, password=password) # user is empty
        print(user)
        if user is not None:
            print('logged in')
            login(request, user)
            return redirect('dashboard')
        else:
            print('an error')
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'login.html')



@login_required(login_url='login')
def dashboard(request):
    user = request.user
    if user.role == 'student':
        return render(request, 'student.html')
    elif user.role == 'staff':
        return render(request, 'staff.html')
    elif user.role == 'admin':
        return render(request, 'admin.html')
    elif user.role == 'editor':
        return render(request, 'editor.html')
    else:
        return redirect('login')
