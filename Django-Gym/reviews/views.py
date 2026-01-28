from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from reviews.models import Review
from reviews.forms import ReviewForm, ReviewPublicForm
from home.decorators import staff_required


def review_index(request):
    reviews = Review.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "reviews/index.html", {"reviews": reviews})


@login_required
def review_submit(request):
    initial_name = request.user.get_full_name() or request.user.username
    if request.method == "POST":
        form = ReviewPublicForm(request.POST, initial={"name": initial_name})
        if form.is_valid():
            review = form.save(commit=False)
            review.is_published = True
            review.save()
            messages.success(request, "Р”СЏРєСѓС”РјРѕ Р·Р° РІС–РґРіСѓРє!")
            return redirect("/reviews")
    else:
        form = ReviewPublicForm(initial={"name": initial_name})

    return render(request, "reviews/submit.html", {"form": form})


@staff_required
def review_list(request):
    reviews = Review.objects.all().order_by("-created_at")
    return render(request, "reviews/list.html", {"reviews": reviews})


@staff_required
def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            messages.success(request, f"Відгук від {review.name} створено")
            return redirect("/reviews/list")
    else:
        form = ReviewForm()

    return render(request, "reviews/create.html", {"form": form})


@staff_required
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            messages.success(request, f"Відгук від {review.name} оновлено")
            return redirect("/reviews/list")
    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/edit.html", {"form": form, "review": review})


@staff_required
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    messages.error(request, f"Відгук від {review.name} видалено")
    return redirect("/reviews/list")
