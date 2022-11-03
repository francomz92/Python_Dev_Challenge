import os

URL_CLIMA = os.getenv('URL_CLIMA')
URL_LOCATION = os.getenv('URL_LOCATION')
API_KEY = os.getenv('API_KEY')

MAX_TEMPERATURE_LIMIT = os.getenv('MAX_TEMPERATURE_LIMIT', 28)