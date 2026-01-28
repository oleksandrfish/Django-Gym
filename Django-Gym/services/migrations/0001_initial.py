from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Назва")),
                ("description", models.TextField(blank=True, verbose_name="Опис")),
                (
                    "duration_minutes",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(15),
                            django.core.validators.MaxValueValidator(240),
                        ],
                        verbose_name="Тривалість (хв)",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Ціна (грн)",
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("B", "Початковий"),
                            ("I", "Середній"),
                            ("A", "Просунутий"),
                        ],
                        default="B",
                        max_length=1,
                        verbose_name="Рівень",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("G", "Груповий клас"),
                            ("P", "Персональний"),
                            ("R", "Recovery"),
                        ],
                        default="G",
                        max_length=1,
                        verbose_name="Категорія",
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="Активний")),
            ],
            options={
                "verbose_name": "Клас",
                "verbose_name_plural": "Класи",
            },
        ),
    ]
