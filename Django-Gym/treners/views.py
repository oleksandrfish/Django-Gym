from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from treners.forms import BarberForm, BookingForm
from treners.models import Barber, Booking
from home.decorators import staff_required
from django.contrib import messages

from favorites.favorites import get_count_of_favorite_barbers, get_favorite_barbers

@staff_required
def barber_list(request):
    barbers = Barber.objects.all()

    return render(request, "barbers/list.html", {"barbers": barbers})

def barber_index(request):
    text = request.GET.get("text", "")

    if text:
        barbers = Barber.objects.filter(name__icontains=text)
    else:
        barbers = Barber.objects.all()

    return render(request, "barbers/index.html", {"barbers": barbers, "fav_count": get_count_of_favorite_barbers(request), "fav_barbers": get_favorite_barbers(request)})

def barber_detail(request, pk):
    barber = get_object_or_404(Barber, pk=pk)
    return render(request, "barbers/detail.html", {"barber": barber})

# метод додавання нового барбера
@staff_required
def barber_create(request):
    # якщо запит є POST, тоді додаємо елемент в базу
    if (request.method == "POST"):
        form = BarberForm(request.POST, request.FILES)
        if form.is_valid():
            barber = form.save()
            messages.success(request, f"Тренера {barber.name} успішно створено")
            return redirect(reverse("barber_detail", args=[barber.pk]))
    else:
        # якщо запит не є POST, тоді показуємо порожню форму
        form = BarberForm()
    return render(request, "barbers/create.html", {"form": form})

@staff_required
def barber_update(request, pk):
    # шукаємо барбера за id
    barber = get_object_or_404(Barber, pk=pk)

    if request.method == "POST":
        # створюємо форму з даними з запиту та існуючого барбера
        form = BarberForm(request.POST, request.FILES, instance=barber)
        if form.is_valid():
            # зберігаємо зміни в базу
            barber = form.save()
            messages.success(request, f"Дані тренера {barber.name} оновлено")
            return redirect(reverse("barber_detail", args=[barber.pk]))
    else:
        # створюємо форму з даними знайденого барбера
        form = BarberForm(instance=barber)

    return render(request, "barbers/edit.html", {"form": form})


@staff_required
def barber_delete(request, pk): 
    barber = get_object_or_404(Barber, pk=pk)
    barber.delete()
    messages.error(request, f"Тренера {barber.name} видалено")
    return redirect('/barbers/list')


@staff_required
def booking_list(request):
    bookings = Booking.objects.select_related("barber").order_by("appointment_date")
    return render(request, "bookings/list.html", {"bookings": bookings})


@staff_required
def booking_create(request):
    lang = request.session.get("lang", "uk")
    if request.method == "POST":
        form = BookingForm(request.POST, lang=lang)
        if form.is_valid():
            booking = form.save()
            messages.success(
                request, f"Запис для {booking.customer_name} успішно створено"
            )
            return redirect("/bookings/list")
    else:
        form = BookingForm(lang=lang)

    return render(request, "bookings/create.html", {"form": form})


@staff_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    lang = request.session.get("lang", "uk")

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking, lang=lang)
        if form.is_valid():
            booking = form.save()
            messages.success(
                request, f"Запис для {booking.customer_name} оновлено"
            )
            return redirect("/bookings/list")
    else:
        form = BookingForm(instance=booking, lang=lang)

    return render(request, "bookings/edit.html", {"form": form, "booking": booking})


@staff_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    messages.error(request, f"Запис для {booking.customer_name} видалено")
    return redirect("/bookings/list")
