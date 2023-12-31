from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
import requests
from datetime import datetime, timedelta
from rest_framework.permissions import IsAuthenticated




class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class WeatherDataView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Retrieve latitude, longitude, and number of days from the query parameters
        latitude = request.query_params.get('latitude')
        longitude = request.query_params.get('longitude')
        num_days = request.query_params.get('num_days', 7)  # Default to 7 days if not provided

        # Calculate start and end dates based on the number of days
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=int(num_days) - 1)

        print(f"Received latitude: {latitude}")
        print(f"Received longitude: {longitude}")
        print(f"Calculated start_date: {start_date}")
        print(f"Calculated end_date: {end_date}")

        # Validate that latitude and longitude are provided
        if not latitude or not longitude:
            return Response({'error': 'Latitude and Longitude are required parameters.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
            api_url += f"&past_days={num_days}&hourly=temperature_2m,precipitation,cloudcover"

            # Make the HTTP request using the requests library
            response = requests.get(api_url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                weather_data = response.json()
                return Response(weather_data, status=status.HTTP_200_OK)
            else:
                return Response({'error': response.text}, status=response.status_code)

        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

