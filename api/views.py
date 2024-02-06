from django.shortcuts import render
from rest_framework import viewsets
from .models import TemperatureForecast
from .serializer import TemperatureForecastSerializer

# CBV - ModelViewSet
# class TemperatureForecastViewset(viewsets.ModelViewSet):
#     queryset = TemperatureForecast.objects.all()
#     serializer_class = TemperatureForecastSerializer

# View to render forecast list page
def index(request):
    return render(request, "api/forecasts.html")