"""
    Ejercicio 1:
        Completar el método is_hot_in_pehuajo con el siguiente objetivo:
        ● Consultar la información de clima y devolver True si la temperatura actual supera los 28
        grados celsius o False caso contrario. Esto implica incluso devolver False ante cualquier
        excepción http
"""
from typing import Tuple

import requests

from core.constants.climates import URL_LOCATION, URL_CLIMA, API_KEY, MAX_TEMPERATURE_LIMIT


class GeoAPI:

    @classmethod
    def is_hot_in_pehuajo(cls) -> bool:
        f"""
            A partir de ._get_coordinates():
                Sin error retorna True si la temperatura actual de Pehuajo es mayor a {MAX_TEMPERATURE_LIMIT},
                En cualquier otro caso retorna False
        """
        error, coordinates = cls._get_coordinates()
        if error:
            return False

        response = requests.get(URL_CLIMA,
                                params={
                                    'lat': coordinates['lat'],
                                    'lon': coordinates['lon'],
                                    'appid': API_KEY,
                                    'lang': 'es',
                                    'units': 'metric',
                                })
        if response.status_code != 200:
            return False

        data = response.json()
        return data['main']['temp'] > MAX_TEMPERATURE_LIMIT

    @classmethod
    def _get_coordinates(cls, city: str = 'Pehuajo', country_code: str = 'ar', limit: int = 1) -> Tuple:
        """
            Obtiene las coordenadas de una ciudad determinada
            @city: str -> Nombre de la ciudad a buscar
            @country_code: str -> Código de pais según la ISO 3166
            @limit: int -> Máxima cantidad de resultados a mostrar

            return:
                    Tuple[0]: bool -> True si hubo un error sino False
                    Tuple[1]: None | dict -> None si hubo un error
        """
        response = requests.get(url=URL_LOCATION, params={
            'q': f'{city}, {country_code}',
            'limit': limit,
            'appid': API_KEY,
        })
        if response.status_code != 200:
            return True, None

        data = response.json()
        return False, {
            'lat': data[0]['lat'],
            'lon': data[0]['lon'],
        }