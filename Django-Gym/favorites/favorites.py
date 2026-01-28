from favorites.models import Favorite

FAVORITE_BARBERS_KEY = "favorite_barbers"


def _is_authenticated(request):
    user = getattr(request, "user", None)
    return bool(user and getattr(user, "is_authenticated", False))


def _get_session_favorites(request):
    return request.session.get(FAVORITE_BARBERS_KEY, [])


def _set_session_favorites(request, favorite_ids):
    request.session[FAVORITE_BARBERS_KEY] = favorite_ids


def _merge_session_to_user(request):
    if not _is_authenticated(request):
        return
    session_ids = _get_session_favorites(request)
    if not session_ids:
        return
    for barber_id in session_ids:
        Favorite.objects.get_or_create(user=request.user, barber_id=barber_id)
    _set_session_favorites(request, [])


def get_favorite_barbers(request):
    if _is_authenticated(request):
        _merge_session_to_user(request)
        return list(
            Favorite.objects.filter(user=request.user).values_list("barber_id", flat=True)
        )
    return _get_session_favorites(request)


def get_count_of_favorite_barbers(request):
    if _is_authenticated(request):
        _merge_session_to_user(request)
        return Favorite.objects.filter(user=request.user).count()
    return len(_get_session_favorites(request))


def add_barber_to_favorites(request, barber_id):
    if _is_authenticated(request):
        Favorite.objects.get_or_create(user=request.user, barber_id=barber_id)
        return
    favorite_ids = _get_session_favorites(request)
    if barber_id not in favorite_ids:
        favorite_ids.append(barber_id)
        _set_session_favorites(request, favorite_ids)


def remove_barber_from_favorites(request, barber_id):
    if _is_authenticated(request):
        Favorite.objects.filter(user=request.user, barber_id=barber_id).delete()
        return
    favorite_ids = _get_session_favorites(request)
    if barber_id in favorite_ids:
        favorite_ids.remove(barber_id)
        _set_session_favorites(request, favorite_ids)
