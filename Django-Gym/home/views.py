from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import login, logout

from treners.models import Booking
from treners.forms import BookingForm
from home.forms import RegisterForm, LoginForm

# Create your views here.
def home(request):
    bookings = Booking.objects.all().order_by("appointment_date")
    return render(request, "home/index.html", {"bookings": bookings})

def book_service(request):
    lang = request.session.get("lang", "uk")
    if request.method == "POST":
        form = BookingForm(request.POST, lang=lang)
        if form.is_valid():
            booking = form.save()
            messages.success(
                request,
                f"Запис для {booking.customer_name} успішно створено.",
            )
            return redirect("home")
    else:
        form = BookingForm(lang=lang)

    return render(request, "home/book.html", {"form": form})


def gallery(request):
    return render(request, "home/gallery.html")


def set_language(request, code):
    if code in ("uk", "en"):
        request.session["lang"] = code
    return redirect(request.META.get("HTTP_REFERER", "/"))


def logout_view(request):
    logout(request)
    return redirect("/")


def register(request):
    lang = request.session.get("lang", "uk")
    if request.method == "POST":
        form = RegisterForm(request.POST, lang=lang)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Акаунт створено успішно.")
            return redirect("home")
    else:
        form = RegisterForm(lang=lang)

    return render(request, "registration/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = LoginForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["lang"] = self.request.session.get("lang", "uk")
        return kwargs

    def form_valid(self, form):
        # Add your authentication logic here
        return super().form_valid(form)
