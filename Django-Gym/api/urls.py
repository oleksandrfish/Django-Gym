from django.contrib import admin
from django.urls import path

import api.views as views 

urlpatterns = [
    path('barbers/', views.BarberList.as_view()),
    path('barbers/<int:pk>', views.BarberDetail.as_view()),
    path('barbers/create', views.BarberList.as_view()),
]
