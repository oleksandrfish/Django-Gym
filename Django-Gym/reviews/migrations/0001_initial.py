from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("name", models.CharField(max_length=100, verbose_name="Ім'я")),
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name="Оцінка",
                    ),
                ),
                ("text", models.TextField(verbose_name="Відгук")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Створено"),
                ),
                ("is_published", models.BooleanField(default=True, verbose_name="Опубліковано")),
            ],
            options={
                "verbose_name": "Відгук",
                "verbose_name_plural": "Відгуки",
            },
        ),
    ]
