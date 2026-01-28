from rest_framework import serializers
from treners.models import Barber

class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = '__all__'
