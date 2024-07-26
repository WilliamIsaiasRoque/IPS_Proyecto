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

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        edad = request.POST['edad']

        if password == confirm_password:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Usuario (nombre, edad, username, contrasena) VALUES (%s, %s, %s, %s)",
                    [username, edad, username, password]
                )
        return login(request)

    return render(request, "register.html")

def logout(request):
    request.session.flush()
    return redirect('index')  # Redirect to the main page after logging out

def prod_list(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Producto ORDER BY nombre")
        prods = cursor.fetchall()
    return render(request, 'productos_list.html', {'prods': prods})

def prod_detail(request, pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Producto WHERE id = %s", [pk])
        prod = cursor.fetchone()
    return render(request, 'productos_detail.html', {'prod': prod})
