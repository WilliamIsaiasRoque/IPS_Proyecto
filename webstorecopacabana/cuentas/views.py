from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = User.objects.create_superuser(username=username, email=email, password=password)
            return render(request, 'cuentas/register.html', {'success': True})
        else:
            return render(request, 'cuentas/register.html', {'error': 'Las contraseñas no coinciden.'})

    return render(request, 'cuentas/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pag_main')
        else:
            return render(request, 'cuentas/login.html', {'error': 'Ingresó algún dato incorrecto.'})

    return render(request, 'cuentas/login.html')

def client_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        user = User.objects.get_or_create(username=username)[0]
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('pag_main')

    return render(request, 'cuentas/client_login.html')

def logout_view(request):
    logout(request)
    return redirect('pag_main')
