from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import TemperatureForecastViewset

router = DefaultRouter()
router.register('', TemperatureForecastViewset)

urlpatterns = [
    path('', include(router.urls))
]
