from django.contrib import admin
from django.urls import path

import favorites.views

urlpatterns = [
    path('', favorites.views.index, name='favorites_index'),
    path('add/<int:barber_id>/<str:return_url>/', favorites.views.add_barber, name='add_fav_barber'),
    path('remove/<int:barber_id>/<str:return_url>/', favorites.views.remove_barber, name='remove_fav_barber'),
]
