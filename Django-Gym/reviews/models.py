from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    rating = models.IntegerField(
        "Оцінка", validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField("Відгук")
    created_at = models.DateTimeField("Створено", auto_now_add=True)
    is_published = models.BooleanField("Опубліковано", default=True)

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"
