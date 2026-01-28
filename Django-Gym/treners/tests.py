from django.test import TestCase

from treners.models import Barber

# Create your tests here.
class BarbersTests(TestCase):
    def test_barber_create(self):
        barber = Barber.objects.create(
            name="John Doe",
            experience=5,
            birthdate="1990-01-01",
            position="J",
            gender="M",
            phone="123-456-7890"
        )

        self.assertEqual(barber.name, "John Doe")
        self.assertEqual(barber.rating, 0)
        self.assertEqual(barber.position, "J")

    def test_barber_str(self):
        barber = Barber.objects.create(
            name="Jane Smith",
            experience=10,
            birthdate="1985-05-15",
            position="S",
            gender="F",
            phone="098-765-4321",
        )

        self.assertEqual(str(barber), "Jane Smith (Senior тренер)")
