from django.shortcuts import render, redirect
from django.db import connection

def index(request):
    return render(request, 'index.html')

def prod_new(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        stock = request.POST.get('stock')
        precio = request.POST.get('precio')
        imagen = request.POST.get('imagen')

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO Producto (nombre, descripcion, stock, precio, imagen) VALUES (%s, %s, %s, %s, %s)",
                           [nombre, descripcion, stock, precio, imagen])
        
        return redirect('prod_list')

    return render(request, 'productos_edit.html')

def prod_edit(request, pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Producto WHERE id = %s", [pk])
        prod = cursor.fetchone()

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        stock = request.POST.get('stock')
        precio = request.POST.get('precio')
        imagen = request.POST.get('imagen')

        with connection.cursor() as cursor:
            cursor.execute("UPDATE Producto SET nombre = %s, descripcion = %s, stock = %s, precio = %s, imagen = %s WHERE id = %s",
                           [nombre, descripcion, stock, precio, imagen, pk])

        return redirect('prod_detail', pk=pk)

    return render(request, 'productos_edit.html', {'prod': prod})

def prod_delete(request, pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Producto WHERE id = %s", [pk])
        prod = cursor.fetchone()

    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM Producto WHERE id = %s", [pk])
        
        return redirect('prod_list')

    return render(request, 'productos_delete.html', {'prod': prod})
