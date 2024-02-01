from django.db import models

# Create your models here.
class TemperatureForecast(models.Model):
    temperature = models.FloatField()
    atmospheric_pressure = models.FloatField()
    humidity = models.FloatField()
    precipitation_percentage = models.FloatField()
    weather_conditions = models.CharField(max_length=150)