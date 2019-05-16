import unittest
from APIConnectionGoogle import APIConnection, localBook, APIServiceExtra
from unittest.mock import patch
import requests
from interface_book import Book

class MockTest(unittest.TestCase):
    """Pruebas unitaria de la Google Books API"""

    @patch('requests.get')
    def test_mock(self, mock_get):
        # casos de prueba
        test_cases = (
        ("el principito", 200, '{"totalItems": 314, "items": [{ "volumeInfo": { "title": "El Principito / The Little Prince", "subtitle": "a", "authors": ["Antoine de Saint-Exupéry"], "publisher": "SELECTOR", "publishedDate": "2004-12-30", "description": "The little prince is the marvellous story of a small boy who comes from a planet barely larger than a house, and who asks questions and seeks answers to things that for adults might be of little importance.", "industryIdentifiers": [{"type": "ISBN_10", "identifier": "9706433910"}], "pageCount": 77, "categories": ["Juvenile Fiction"], "imageLinks": {"smallThumbnail": "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=5&source=gbs_api", "thumbnail": "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=1&source=gbs_api"}, "previewLink": "http://books.google.com.mx/books?id=CpvT1p6LHnoC&dq=El+principito+/+the+little+prince&hl=&cd=1&source=gbs_api"}, "accessInfo": {"pdf": {"isAvailable": False}}}]}' ,
        {"totalItems": 314, "items": [{"volumeInfo": {"title": "El Principito / The Little Prince", "subtitle": "a", "authors": ["Antoine de Saint-Exupéry"], "publisher": "SELECTOR", "publishedDate": "2004-12-30", "description":
        "The little prince is the marvellous story of a small boy who comes from a planet barely larger than a house, and who asks questions and seeks answers to things that for adults might be of little importance.",
        "industryIdentifiers": [{"type": "ISBN_10", "identifier": "9706433910"}], "pageCount": 77, "categories": ["Juvenile Fiction"], "imageLinks": {"smallThumbnail":
        "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=5&source=gbs_api", "thumbnail": "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        },"previewLink": "http://books.google.com.mx/books?id=CpvT1p6LHnoC&dq=El+principito+/+the+little+prince&hl=&cd=1&source=gbs_api"}, "accessInfo": {"pdf": {"isAvailable": False}}}]},
        [Book("El Principito / The Little Prince", "a", ["Antoine de Saint-Exupéry"], "SELECTOR", "2004-12-30",
        "The little prince is the marvellous story of a small boy who comes from a planet barely larger than a house, and who asks questions and seeks answers to things that for adults might be of little importance.", "9706433910",
        77, ["Juvenile Fiction"], "http://books.google.com/books/content?id=CpvT1p6LHnoC&printsec=frontcover&img=1&zoom=1&source=gbs_api",
        "http://books.google.com.mx/books?id=CpvT1p6LHnoC&dq=El+principito+/+the+little+prince&hl=&cd=1&source=gbs_api", False, "no identificado")]),

        ("el principito", 404, '404 page not found', "", "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"),

        ("el principito", 500, '500 internal server error', "", "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"),

        ("fdshjoaowl", 200, '{"kind": "books#volumes", "totalItems": 0}', {"kind": "books#volumes", "totalItems": 0}, None),

        ("", 400, '', '', "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"))

        for entrada, stat, mock_text, mock_json, esperado in test_cases:
            mock_get.return_value.status_code = stat # creamos mock del status
            mock_get.return_value.json = lambda : mock_json # creamos un mock de la salida esperada
            salida_real = APIConnection().getBook(entrada, APIServiceExtra())
            # comparamos salida real con esperada
            self.assertEqual(salida_real, esperado)

    def testGetBook(self):
        """Test de los libros"""
        # salidas esperadas de la función getBook
        salida_esperadas = (("GOT", [Book("I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=GOT&hl=&cd=7&source=gbs_api', True ,'no identificado')]),

        ("fdshjoaowl", None),

        ("", "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"))

        for entrada, salida in salida_esperadas:
            # comparaciones de la salida real con la esperada
            salida_real = APIConnection().getBook(entrada, APIServiceExtra())
            self.assertEqual(salida, salida_real)

if __name__ == "__main__":
    unittest.main()
