from django.shortcuts import render
from rest_framework import viewsets
from .models import TemperatureForecast
from .serializer import TemperatureForecastSerializer

# Create your views here.
class TemperatureForecastViewset(viewsets.ModelViewSet):
    queryset = TemperatureForecast.objects.all()
    serializer_class = TemperatureForecastSerializer