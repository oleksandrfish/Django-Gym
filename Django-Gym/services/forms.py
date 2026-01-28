from django import forms
from django.forms import ModelForm

from services.models import Service


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = [
            "name",
            "description",
            "duration_minutes",
            "price",
            "level",
            "category",
            "active",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Назва класу"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Короткий опис класу",
                }
            ),
            "duration_minutes": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "60"}
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "399"}
            ),
            "level": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
