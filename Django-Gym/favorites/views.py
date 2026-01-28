from django.shortcuts import redirect, render

from treners.models import Barber
from favorites.favorites import (
    add_barber_to_favorites,
    get_favorite_barbers,
    remove_barber_from_favorites,
)


def index(request):
    favoriteIds = get_favorite_barbers(request)
    if favoriteIds:
        barbers = Barber.objects.filter(id__in=favoriteIds)
    else:
        barbers = Barber.objects.none()
    return render(request, "favorites/index.html", {"barbers": barbers})

def add_barber(request, barber_id, return_url):
    add_barber_to_favorites(request, barber_id)
    return redirect(return_url)

def remove_barber(request, barber_id, return_url):
    remove_barber_from_favorites(request, barber_id)
    return redirect(return_url)
