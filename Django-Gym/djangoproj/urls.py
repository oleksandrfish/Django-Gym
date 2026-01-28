from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from djangoproj import settings
from home.views import CustomLoginView
from treners import views as treners_views

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('favorites/', include('favorites.urls')),
    path('barbers/', include('treners.urls')),
    path('services/', include('services.urls')),
    path('reviews/', include('reviews.urls')),
    path('bookings/list', treners_views.booking_list),
    path('bookings/create', treners_views.booking_create),
    path('bookings/edit/<int:pk>/', treners_views.booking_update),
    path('bookings/delete/<int:pk>/', treners_views.booking_delete),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('api/', include('api.urls')),
]

if settings.DEBUG:                                         
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
