from favorites.favorites import get_count_of_favorite_barbers

def favorite_barbers_count(request):
    return { 'fav_count': get_count_of_favorite_barbers(request) }