from django.urls import path
from . import views

urlpatterns = [
    path('', views.pag_main, name='pag_main'),
    path('prods/list/', views.prod_list, name='prod_list'),
    path('prods/<int:pk>/', views.prod_detail, name='prod_detail'),
    path('prods/new/', views.prod_new, name='prod_new'),
    path('prods/<int:pk>/edit/', views.prod_edit, name='prod_edit'),
    path('prods/<int:pk>/delete/', views.prod_delete, name='prod_delete'),
]

