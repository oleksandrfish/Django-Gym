from django.contrib import admin
from django.urls import path

from treners import views

urlpatterns = [
    path('', views.barber_index, name="barber_index"),
                                                                          
    path('list', views.barber_list),
    path('<int:pk>/', views.barber_detail, name="barber_detail"),
    path('delete/<int:pk>/', views.barber_delete),
    path('create', views.barber_create),
    path('edit/<int:pk>/', views.barber_update),
]
