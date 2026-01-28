from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from home.translations import get_translations


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        lang = kwargs.pop("lang", "uk")
        super().__init__(request, *args, **kwargs)
        t = get_translations(lang)
        self.fields["username"].label = t["auth_username"]
        self.fields["password"].label = t["auth_password"]
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": t["auth_username_placeholder"]}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": t["auth_password_placeholder"]}
        )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        lang = kwargs.pop("lang", "uk")
        super().__init__(*args, **kwargs)
        t = get_translations(lang)
        self.fields["username"].label = t["auth_username"]
        self.fields["password1"].label = t["auth_password"]
        self.fields["password2"].label = t["auth_password_confirm"]
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": t["auth_username_placeholder"]}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": t["auth_password_placeholder"]}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": t["auth_password_confirm_placeholder"]}
        )
