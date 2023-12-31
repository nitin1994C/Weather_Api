
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

class UserRegistrationViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = '/register/'

    def test_user_registration_successful(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {'message': 'User registered successfully'})

    def test_user_registration_invalid_data(self):
        data = {
            'username': 'testuser',
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class WeatherDataViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.weather_url = '/weather/'

    def test_weather_data_retrieval(self):
        # Assuming you have a user for authentication
        user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=user)

        data = {
            'latitude': '52.52',
            'longitude': '13.41',
            'num_days': '7',
        }
        response = self.client.get(self.weather_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add more assertions based on the expected structure of the API response
        self.assertIn('hourly', response.data)

    def test_weather_data_invalid_parameters(self):
        response = self.client.get(self.weather_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Add more assertions based on the expected error response
        self.assertIn('error', response.data)
        
        
