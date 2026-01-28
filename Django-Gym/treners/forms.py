from django import forms
from django.forms import ModelForm
from treners.models import Barber, Booking
from home.translations import get_translations

class BarberForm(ModelForm):
    class Meta:
        model = Barber
        fields = ["name", "photo", "experience", "birthdate", "position", "gender", "phone"]
        widgets = {
            'birthdate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            "photo": forms.ClearableFileInput(attrs={'class': 'form-control'}),
            "position": forms.Select(attrs={'class': 'form-select'}),
            "gender": forms.Select(attrs={'class': 'form-select'}),
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Введіть ім'я тренера"}),
            "experience": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Вкажіть стаж у роках'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Номер телефону', "type": "tel"}),
        }


class BookingForm(ModelForm):
    appointment_date = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={"class": "form-control", "type": "datetime-local"},
            format="%Y-%m-%dT%H:%M",
        ),
    )

    def __init__(self, *args, **kwargs):
        lang = kwargs.pop("lang", "uk")
        super().__init__(*args, **kwargs)
        self.fields["barber"].queryset = Barber.objects.order_by("name")

        t = get_translations(lang)
        self.fields["customer_name"].label = t["form_customer_name"]
        self.fields["contact_phone"].label = t["form_contact_phone"]
        self.fields["appointment_date"].label = t["form_appointment_date"]
        self.fields["barber"].label = t["form_trainer"]

        self.fields["customer_name"].widget.attrs["placeholder"] = t[
            "form_customer_name_placeholder"
        ]
        self.fields["contact_phone"].widget.attrs["placeholder"] = t[
            "form_contact_phone_placeholder"
        ]

    class Meta:
        model = Booking
        fields = ["customer_name", "contact_phone", "appointment_date", "barber"]
        labels = {
            "customer_name": "Ім'я клієнта",
            "contact_phone": "Телефон",
            "appointment_date": "Дата та час",
            "barber": "Тренер",
        }
        widgets = {
            "customer_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ваше ім'я"}
            ),
            "contact_phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "+38 (0__) ___ __ __", "type": "tel"}
            ),
            "barber": forms.Select(attrs={"class": "form-select"}),
        }
    
# class BarberSearchForm(forms.Form):
#     text = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search barbers...'}))
