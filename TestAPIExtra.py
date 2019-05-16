import unittest
from APIConnectionGoogle import APIServiceExtra
from unittest.mock import patch
import requests

class MockTest(unittest.TestCase):
    """Pruebas unitarias de la Open Library API"""

    @patch('requests.get')
    def test_mock(self, mock_get):
        # casos de prueba
        test_cases = (("9706433910", 200, '''{"ISBN:9706433910": {"publishers": [{"name": "Selector"}], "identifiers": {"isbn_13": ["9789706433916"], "openlibrary":
        ["OL13153378M"], "isbn_10": ["9706433910"], "goodreads": ["43247"]}, "weight": "3.2 ounces", "title": "El Principito / The Little Prince", "url":
        "https://openlibrary.org/books/OL13153378M/El_Principito_The_Little_Prince", "number_of_pages": 77, "cover": {"small": "https://covers.openlibrary.org/b/id/5253108-S.jpg",
        "large": "https://covers.openlibrary.org/b/id/5253108-L.jpg", "medium": "https://covers.openlibrary.org/b/id/5253108-M.jpg"}, "publish_date": "December 30, 2004",
        "key": "/books/OL13153378M"}}''',
        {"ISBN:9706433910": {"publishers": [{"name": "Selector"}], "identifiers": {"isbn_13": ["9789706433916"], "openlibrary":
        ["OL13153378M"], "isbn_10": ["9706433910"], "goodreads": ["43247"]}, "weight": "3.2 ounces", "title": "El Principito / The Little Prince", "url":
        "https://openlibrary.org/books/OL13153378M/El_Principito_The_Little_Prince", "number_of_pages": 77, "cover": {"small": "https://covers.openlibrary.org/b/id/5253108-S.jpg",
        "large": "https://covers.openlibrary.org/b/id/5253108-L.jpg", "medium": "https://covers.openlibrary.org/b/id/5253108-M.jpg"}, "publish_date": "December 30, 2004",
        "key": "/books/OL13153378M"}},
        "3.2 ounces"),

        ("8429150943", 200, '''{"ISBN:8429150943": {"publishers": [{"name": "Revert\u00e9"}], "title": "Probabilidad y estadistica para ingenieros", "url":
        "https://openlibrary.org/books/OL26393465M/Probabilidad_y_estadistica_para_ingenieros", "identifiers": {"isbn_13": ["9788429150940"], "openlibrary":
        ["OL26393465M"]}, "cover": {"small": "https://covers.openlibrary.org/b/id/8088548-S.jpg", "large": "https://covers.openlibrary.org/b/id/8088548-L.jpg",
        "medium": "https://covers.openlibrary.org/b/id/8088548-M.jpg"}, "publish_date": "1963", "key": "/books/OL26393465M"}}''',
        {"ISBN:8429150943": {"publishers": [{"name": "Revert\u00e9"}], "title": "Probabilidad y estadistica para ingenieros", "url":
        "https://openlibrary.org/books/OL26393465M/Probabilidad_y_estadistica_para_ingenieros", "identifiers": {"isbn_13": ["9788429150940"], "openlibrary":
        ["OL26393465M"]}, "cover": {"small": "https://covers.openlibrary.org/b/id/8088548-S.jpg", "large": "https://covers.openlibrary.org/b/id/8088548-L.jpg",
        "medium": "https://covers.openlibrary.org/b/id/8088548-M.jpg"}, "publish_date": "1963", "key": "/books/OL26393465M"}} ,"no identificado"),

        ("hola", 200, '{}', {}, "HA OCURRIDO UN ERROR"),

        ("9706433910", 404, '404 page not found', "", "HA OCURRIDO UN ERROR"),

        ("9706433910", 500, '500 internal server error', "", "HA OCURRIDO UN ERROR"),

        ("", 400, '', '', "HA OCURRIDO UN ERROR"))


        for entrada, stat, mock_text, mock_json, esperado in test_cases:
            mock_get.return_value.status_code = stat # creamos mock del status
            mock_get.return_value.json = lambda : mock_json  # creamos mock de la salida
            salida_real = APIServiceExtra().getExtras(entrada)
            # comparamos salida esperada con salida real
            self.assertEqual(salida_real, esperado)

    def test_Get_Extras(self):
        # casos de prueba
        test_cases = (("9706433910", "3.2 ounces"),

        ("8429150943", "no identificado"),

        ("", "HA OCURRIDO UN ERROR"),

        ("-----", "HA OCURRIDO UN ERROR"),

        ("abcd", "HA OCURRIDO UN ERROR"))

        for entrada, salida_esperada in test_cases:
            # comparamos salida real con salida esperada
            salida_real = APIServiceExtra().getExtras(entrada)
            self.assertEqual(salida_real, salida_esperada)

if __name__ == "__main__":
    unittest.main()
