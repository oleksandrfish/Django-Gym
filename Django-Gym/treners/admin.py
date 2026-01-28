from django.contrib import admin

from treners.models import Barber, Booking

class BarberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'experience']
    search_fields = ['name', 'position']
    list_filter = ['position']

# Register your models here.
admin.site.register(Barber, BarberAdmin)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["customer_name", "barber", "appointment_date", "contact_phone"]
    search_fields = ["customer_name", "contact_phone", "barber__name"]
    list_filter = ["appointment_date", "barber"]

admin.site.site_header = "PowerGym Адмінка"
admin.site.site_title = "PowerGym"
admin.site.index_title = "Керування тренерами"
