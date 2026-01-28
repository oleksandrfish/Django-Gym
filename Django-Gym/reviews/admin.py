from django.contrib import admin

from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name", "rating", "created_at", "is_published"]
    list_filter = ["rating", "is_published", "created_at"]
    search_fields = ["name", "text"]
