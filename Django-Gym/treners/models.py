from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

class Barber(models.Model):
    GENDER_CHOICES = [
        ('M', 'Чоловік'),
        ('F', 'Жінка')
    ]
    POSITION_CHOICES = [
        ('J', 'Junior тренер'),
        ('S', 'Senior тренер'),
        ('M', 'Master тренер')
    ]

    name = models.CharField("Ім'я", max_length=100)
    photo = models.ImageField("Фото", upload_to='treners_photos/', blank=True, null=True)
    experience = models.IntegerField(
        "Стаж (років)", validators=[MinValueValidator(0), MaxValueValidator(60)]
    )
    birthdate = models.DateField("Дата народження")
    position = models.CharField("Спеціалізація", max_length=100, choices=POSITION_CHOICES)
    gender = models.CharField("Стать", max_length=1, choices=GENDER_CHOICES)
    rating = models.FloatField("Рейтинг", default=0)
    phone = models.CharField("Телефон", max_length=20)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренери"

    def __str__(self):
        return f"{self.name} ({self.get_position_display()})"
    
class Booking(models.Model):
    barber = models.ForeignKey(
        Barber, on_delete=models.CASCADE, related_name="bookings", verbose_name="Тренер"
    )
    customer_name = models.CharField("Ім'я клієнта", max_length=100)
    appointment_date = models.DateTimeField("Дата та час")
    contact_phone = models.CharField("Телефон", max_length=20)

    class Meta:
        verbose_name = "Запис"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"Запис для {self.customer_name} з {self.barber.name} на {self.appointment_date}"
