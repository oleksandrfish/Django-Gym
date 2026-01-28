from django.contrib import admin

from services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "level", "duration_minutes", "price", "active"]
    search_fields = ["name", "category"]
    list_filter = ["category", "level", "active"]
