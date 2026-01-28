from django.urls import path

from reviews import views

urlpatterns = [
    path("", views.review_index, name="review_index"),
    path("submit", views.review_submit, name="review_submit"),
    path("list", views.review_list),
    path("create", views.review_create),
    path("edit/<int:pk>/", views.review_update),
    path("delete/<int:pk>/", views.review_delete),
]
