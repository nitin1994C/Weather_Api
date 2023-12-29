from django.urls import path
from .views import UserRegistrationView, WeatherDataView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('weather/', WeatherDataView.as_view(), name='weather_api'),
]
