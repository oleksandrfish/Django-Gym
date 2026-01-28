from django.contrib import admin
from django.urls import path
import home.views

urlpatterns = [
    path('', home.views.home, name='home'),
    path('book', home.views.book_service, name='book'),
    path('gallery', home.views.gallery, name='gallery'),
    path('lang/<str:code>/', home.views.set_language, name='set_language'),
    path('register', home.views.register, name='register'),
    path('logout', home.views.logout_view, name='logout'),
]
