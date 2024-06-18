from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def pag_main(request):
    return render(request, 'index.html')