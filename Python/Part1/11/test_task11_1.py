import unittest
from task11_1_function import *

class FormatCityCountryTestCase(unittest.TestCase):
    """
    Тесты для 'task11_1.py'
    """
    def test_city_country(self):
        """Вывод типа 'Город'?"""
        city_country = get_formatted_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile.')
    
    def test_city_country_population(self):
        """Вывод типа 'Город, Страна – 31231231'?"""
        city_country = get_formatted_city_country('santiago', 'chile', 150000)
        self.assertEqual(city_country, 'Santiago, Chile – 150000.')

unittest.main()