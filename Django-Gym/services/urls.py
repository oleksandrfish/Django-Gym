from django.urls import path

from services import views

urlpatterns = [
    path("", views.service_index, name="service_index"),
    path("list", views.service_list),
    path("create", views.service_create),
    path("edit/<int:pk>/", views.service_update),
    path("delete/<int:pk>/", views.service_delete),
]
