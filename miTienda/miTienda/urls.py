"""
URL configuration for miTienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cliente import views as client

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', client.index, name = 'index'),
    path('login/', client.login, name = 'login'),
    path('register/', client.register, name = 'register'),
    path('logout/', client.logout, name='logout'),
    path('prods/list/', client.prod_list, name='prod_list'),
    path('prods/<int:pk>/', client.prod_detail, name='prod_detail'),
]
