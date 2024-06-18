# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import connection
from django.db.utils import OperationalError

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        edad = request.POST['edad']

        if password == confirm_password:
            try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Usuario (nombre, edad, username, contrasena) VALUES (%s, %s, %s, %s)",
                        [username, edad, username, password]
                    )
            except OperationalError as e:
                return render(request, 'cuentas/register.html', {'error': str(e)})
            
            return render(request, 'cuentas/register.html', {'success': True})
        else:
            return render(request, 'cuentas/register.html', {'error': 'Las contraseñas no coinciden.'})

    return render(request, 'cuentas/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, username, contrasena FROM Usuario WHERE username = %s AND contrasena = %s",
                    [username, password]
                )
                user = cursor.fetchone()
        except OperationalError as e:
            return render(request, 'cuentas/login.html', {'error': str(e)})
        
        if user:
            user = User(id=user[0], username=user[1])
            login(request, user)
            return redirect('pag_main')
        else:
            return render(request, 'cuentas/login.html', {'error': 'Ingresó algún dato incorrecto.'})

    return render(request, 'cuentas/login.html')

def logout_view(request):
    logout(request)
    return redirect('pag_main')

def client_login(request):
    if request.method == 'POST':
        username = request.POST['username']

        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, username FROM Usuario WHERE username = %s",
                    [username]
                )
                user = cursor.fetchone()
        except OperationalError as e:
            return render(request, 'cuentas/client_login.html', {'error': str(e)})

        if user:
            user = User(id=user[0], username=user[1])
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('pag_main')
        else:
            return render(request, 'cuentas/client_login.html', {'error': 'Usuario no encontrado.'})

    return render(request, 'cuentas/client_login.html')


    