# Django Weather API

## Overview

This Django project provides an API for retrieving historic weather data based on location (latitude and longitude) and the number of days in the past. 
The application integrates with the Open Meto API to fetch hourly temperature, precipitation, and cloud cover data.


### Frameworks and Libraries

- **Django**: Chosen as the main web framework for its simplicity, robustness, and extensive community support.
- **Django REST framework (DRF)**: Used for building RESTful APIs in a clean and efficient manner.
- **Requests**: Utilized for making HTTP requests to the Open Meto API.

### API Integration

- Open Meto API (https://open-meteo.com/) is used to obtain historic weather data.
- The API endpoint is constructed dynamically based on user input (latitude, longitude, number of days).

### Security

- **User Registration and Authentication**: Implemented using Django REST framework.
- **JWT Authorization**: Secure endpoints require a valid token for access.

### Database

- MySQL is used as the default database for simplicity, but you can easily switch to another database like PostgreSQL for production.


### Prerequisites

- Python (version 3.x)
- Pipenv (optional but recommended for virtual environment management)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nitin1994C/Weather_Api.git
   cd django-weather-api
2. pip install -r requirements.txt

3.python manage.py migrate

4.python manage.py runserver

### API Endpoints

Weather Data: http://localhost:8000/api/weather/
User Registration: http://localhost:8000/api/register/
User Authentication  Token Obtain View : http://localhost:8000/api/token/
Refresh token :http://localhost:8000/api/token/refresh/

### Notes
Don't forget to set your SECRET_KEY and other sensitive settings in the settings.py file.
Customize the database settings for production use.
Ensure proper security measures are taken in a production environment (e.g., HTTPS, secure passwords).
