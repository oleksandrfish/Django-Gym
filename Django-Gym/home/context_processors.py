from home.translations import get_translations


def ui_text(request):
    lang = request.session.get("lang", "uk")
    if lang not in ("uk", "en"):
        lang = "uk"
    return {"t": get_translations(lang), "lang": lang}
