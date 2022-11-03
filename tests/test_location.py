import requests

from core.constants.climates import API_KEY, URL_LOCATION
from core.climates import GeoAPI


class TestLocation:

    def __init__(self) -> None:
        self.test_get_coordinates()

    def test_get_coordinates(self):
        """ Prueba el metodo para obtener coordenadas """
        response = requests.get(URL_LOCATION, params={
            'q': f'London',
            'limit': 1,
            'appid': API_KEY,
        })
        data = response.json()
        _response = GeoAPI._get_coordinates(city='London', country_code='gb')
        error = _response[0]
        coord = _response[1]
        assert error == False, 'Error'
        if not error:
            assert data[0]['lat'] == coord['lat'], 'Error'
            assert data[0]['lon'] == coord['lon'], 'Error'
        print('Success')
