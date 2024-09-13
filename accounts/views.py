from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import make_password

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )
        login(request, user)
        return redirect('about')
    return render(request, 'accounts/register.html')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
