from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.sessions.models import Session

def index(request):
    return render(request, 'index.html')

def existe(username, password):
    with connection.cursor() as cursor:
        cursor.execute("SELECT username FROM usuario WHERE username=%s AND contrasena=%s", (username, password))
        result = cursor.fetchone()
        return result is not None

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if existe(username, password):
            request.session['is_logged_in'] = True
            request.session['username'] = username
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('index')  # Redirect to the main page after logging out
