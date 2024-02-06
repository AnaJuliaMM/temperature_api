from django.shortcuts import render
from rest_framework import viewsets
from .models import TemperatureForecast
from .serializer import TemperatureForecastSerializer

# CBV - ModelViewSet
# class TemperatureForecastViewset(viewsets.ModelViewSet):
#     queryset = TemperatureForecast.objects.all()
#     serializer_class = TemperatureForecastSerializer

def index(request):
    latest_question_list = TemperatureForecast.objects.all()
    context = {"latest_question_list": latest_question_list}
    return render(request, "api/index.html", context)