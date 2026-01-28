from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from services.models import Service
from services.forms import ServiceForm
from home.decorators import staff_required


def service_index(request):
    services = Service.objects.filter(active=True).order_by("category", "name")
    return render(request, "services/index.html", {"services": services})


@staff_required
def service_list(request):
    services = Service.objects.all().order_by("name")
    return render(request, "services/list.html", {"services": services})


@staff_required
def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save()
            messages.success(request, f"Клас {service.name} створено")
            return redirect("/services/list")
    else:
        form = ServiceForm()

    return render(request, "services/create.html", {"form": form})


@staff_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save()
            messages.success(request, f"Клас {service.name} оновлено")
            return redirect("/services/list")
    else:
        form = ServiceForm(instance=service)

    return render(
        request, "services/edit.html", {"form": form, "service": service}
    )


@staff_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    messages.error(request, f"Клас {service.name} видалено")
    return redirect("/services/list")
