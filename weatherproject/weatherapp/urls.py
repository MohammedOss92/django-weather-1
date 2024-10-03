from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('api/weather/', WeatherAPIView.as_view(), name='weather-api'),
]