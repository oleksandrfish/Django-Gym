from django import forms
from django.forms import ModelForm

from reviews.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["name", "rating", "text", "is_published"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ім'я клієнта"}
            ),
            "rating": forms.Select(
                attrs={"class": "form-select"},
                choices=[(i, f"{i}/5") for i in range(1, 6)],
            ),
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Текст відгуку",
                }
            ),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class ReviewPublicForm(ModelForm):
    class Meta:
        model = Review
        fields = ["name", "rating", "text"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Р†Рј'СЏ РєР»С–С”РЅС‚Р°"}
            ),
            "rating": forms.Select(
                attrs={"class": "form-select"},
                choices=[(i, f"{i}/5") for i in range(1, 6)],
            ),
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "РўРµРєСЃС‚ РІС–РґРіСѓРєСѓ",
                }
            ),
        }
