from django.contrib import admin
from django.urls import path, include
from . import views

# CBV - ModelViewSet
# from rest_framework.routers import DefaultRouter
# from api.views import TemperatureForecastViewset

# router = DefaultRouter()
# router.register('', TemperatureForecastViewset)

urlpatterns = [
    path('', views.index, name="login")
]
