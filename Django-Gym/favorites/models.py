from django.conf import settings
from django.db import models

from treners.models import Barber


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorite_barbers",
    )
    barber = models.ForeignKey(
        Barber,
        on_delete=models.CASCADE,
        related_name="favorited_by",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "barber")

    def __str__(self):
        return f"{self.user} → {self.barber}"
