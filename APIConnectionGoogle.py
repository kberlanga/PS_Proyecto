from abc import ABC, abstractmethod
from interface_book import APIService,Book,APIServiceExtra
from DataBase import DataBase
import requests
import json

class localBook(Book):

    def __init__(self, title, subtitle, authors, publisher, publishedDate, description, isbn_10, numberPages, categories, image, link, pdf, weight):
        Book.__init__(self, title, subtitle, authors, publisher, publishedDate, description, isbn_10, numberPages, categories, image, link, pdf, weight)


class APIConnection(APIService):
    def getBook(self, word, serviceEx):
        """ Función que hace la solicitud a la API Google Books recibiendo como parámetro el nombre del libro que se quiere buscar
        y regresa los datos obtenidos"""
        # Se hace la solicitud de datos a la API
        response = requests.get(url = "https://www.googleapis.com/books/v1/volumes?q=" + str(word))
        # Se verifica si en la ejecución de la solicitud hubo algun error
        if response.status_code != 200:
            return "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"
        else: # Si no es así, procedemos a la extracción de los datos
            if response.json()['totalItems'] == 0:
                return None
            else:
                # Se crea una lista en donde se guardarán los objetos tipo localBook
                list_books = []
                for book in response.json()['items']: # Por cada libro que se regresó extraeamos los datos necesarios
                    # Título del libro
                    title = book['volumeInfo']['title']

                    # Subtítulo del libro
                    if 'subtitle' in book['volumeInfo']:
                        subtitle = book['volumeInfo']['subtitle']
                    else:
                        subtitle = ''

                    # Autor(es) del libro: lista[]
                    if 'authors' in book['volumeInfo']:
                        authors = book['volumeInfo']['authors']
                    else:
                        authors = ''

                    # Editorial del libro
                    if 'publisher' in book['volumeInfo']:
                        publisher = book['volumeInfo']['publisher']
                    else:
                        publisher = ''

                    # Fecha de publicación
                    if 'publishedDate' in book['volumeInfo']:
                        publishedDate = book['volumeInfo']['publishedDate']
                    else:
                        publishedDate = ''

                    # Breve descripción
                    if 'description' in book['volumeInfo']:
                        description = book['volumeInfo']['description']
                    else:
                        description = ''

                    # ISBN (10)
                    if 'industryIdentifiers' in book['volumeInfo']:
                        isbn_10 = book['volumeInfo']['industryIdentifiers'][0]['identifier']
                        weight = serviceEx.getExtras(isbn_10)
                    else:
                        isbn_10 = ''

                    # Número de páginas
                    if 'pageCount' in book['volumeInfo']:
                        numberPages = book['volumeInfo']['pageCount']
                    else:
                        numberPages = ''

                    # Categorías: lista[]
                    if 'categories' in book['volumeInfo']:
                        categories = book['volumeInfo']['categories']
                    else:
                        categories = ''

                    # Imagen de la portada
                    if 'imageLinks' in book['volumeInfo']:
                        if 'thumbnail' in book['volumeInfo']['imageLinks']:
                            image = book['volumeInfo']['imageLinks']['thumbnail']
                        else:
                            image = ''

                    # Link del libro
                    if 'previewLink' in book['volumeInfo']:
                        link = book['volumeInfo']['previewLink']
                    else:
                        link = ''

                    # Está disponible en pdf (?): True | False
                    if 'accessInfo' in book:
                        if 'pdf' in book['accessInfo']:
                            if 'isAvailable' in book['accessInfo']['pdf']:
                                pdf = book['accessInfo']['pdf']['isAvailable']
                            else:
                                pdf = ''

                    # Sólo se guardan los libros que contengan todos los datos, a excepción del subtítulo
                    if title != '' and authors != '' and publisher != '' and publishedDate != '' and description != '' and isbn_10 != '' and numberPages != '' and categories !='' and image != '' and link != '' and pdf != '':
                        # Aquí se crearán los objetos y se agregan a la lista de libros que va a regresar esta función
                        local_book = localBook(title, subtitle, authors, publisher, publishedDate, description, isbn_10, numberPages, categories, image, link, pdf, weight)
                        list_books.append(local_book)


            return list_books

def get_book(nameBook, className):
    className.getBook(nameBook)

class APIServiceExtra(APIServiceExtra):

    def getExtras(self, isbn):
        """Regresa una lista de información extra que se obtiene de una nueva API.
        La clase que se conecta a la API implementa esta clase"""
        # Se hace la solicitud de datos a la API
        response = requests.get(url = "https://openlibrary.org/api/books?bibkeys=ISBN:"+str(isbn)+",&jscmd=data&format=json")

        # Se revisa que la solicitud se haya realizado correctamente
        try:
            if response.status_code != 200 or response.json() == {}:
                return "HA OCURRIDO UN ERROR"
            else:
                weight = response.json()["ISBN:"+str(isbn)]['weight']
        except:
            weight = "no identificado"
        return weight
