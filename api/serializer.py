from rest_framework import serializers
from .models import TemperatureForecast

class TemperatureForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureForecast
        fields = '__all__'
