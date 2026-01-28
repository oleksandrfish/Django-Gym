from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Service(models.Model):
    LEVEL_CHOICES = [
        ("B", "Початковий"),
        ("I", "Середній"),
        ("A", "Просунутий"),
    ]
    CATEGORY_CHOICES = [
        ("G", "Груповий клас"),
        ("P", "Персональний"),
        ("R", "Recovery"),
    ]

    name = models.CharField("Назва", max_length=100)
    description = models.TextField("Опис", blank=True)
    duration_minutes = models.IntegerField(
        "Тривалість (хв)",
        validators=[MinValueValidator(15), MaxValueValidator(240)],
    )
    price = models.DecimalField(
        "Ціна (грн)",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    level = models.CharField("Рівень", max_length=1, choices=LEVEL_CHOICES, default="B")
    category = models.CharField(
        "Категорія", max_length=1, choices=CATEGORY_CHOICES, default="G"
    )
    active = models.BooleanField("Активний", default=True)

    class Meta:
        verbose_name = "Клас"
        verbose_name_plural = "Класи"

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
