                                             

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0004_booking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barber',
            options={'verbose_name': 'Тренер', 'verbose_name_plural': 'Тренери'},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Запис', 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterField(
            model_name='barber',
            name='birthdate',
            field=models.DateField(verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='experience',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(60)], verbose_name='Стаж (років)'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='gender',
            field=models.CharField(choices=[('M', 'Чоловік'), ('F', 'Жінка')], max_length=1, verbose_name='Стать'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='name',
            field=models.CharField(max_length=100, verbose_name="Ім'я"),
        ),
        migrations.AlterField(
            model_name='barber',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='barber_photos/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='position',
            field=models.CharField(choices=[('J', 'Junior тренер'), ('S', 'Senior тренер'), ('M', 'Master тренер')], max_length=100, verbose_name='Спеціалізація'),
        ),
        migrations.AlterField(
            model_name='barber',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='appointment_date',
            field=models.DateTimeField(verbose_name='Дата та час'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='barber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='barbers.barber', verbose_name='Тренер'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contact_phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='customer_name',
            field=models.CharField(max_length=100, verbose_name="Ім'я клієнта"),
        ),
    ]
