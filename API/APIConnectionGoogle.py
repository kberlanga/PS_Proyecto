from abc import ABC, abstractmethod
from interface_book import APIService,Book
from DataBase import DataBase
import requests
import json

class localBook(Book):

    def __init__(self,title, subtitle, authors, publisher, publishedDate, description, isbn_10, numberPages, categories, image, link, pdf):
        Book.__init__(self,title, subtitle, authors, publisher, publishedDate, description, isbn_10, numberPages, categories, image, link, pdf)


class APIConnection(APIService):
    def getBook(self, word):
        """ Función que hace la solicitud a la API Google Books recibiendo como parametro el nombre del libro que se quiere buscar
        y regresa los datos obtenidos"""
        #Se hace la solicitud de datos a la API
        response = requests.get(url = "https://www.googleapis.com/books/v1/volumes?q=" + str(word))
        #Se verifica si en la ejecucion de la solicitud hubo algun error
        if response.status_code != 200:
            return "LA SOLICITUD NO SE EJECUTÓ DE MANERA CORRECTA"
        else: #si no es asi, procedemos a la extraccion de los datos
            if response == None:
                #Si la respuesta de la API esta vacia, se regresa la variable response (None)
                return response
            else:
                #Se crea una lista en donde se guardarán los objetos tipo localBook
                list_books = []
                for book in response.json()['items']: #Por cada libro que se regresó extraeamos los datos necesarios
                    #Título del libro
                    title = book['volumeInfo']['title']

                    #Subtitulo del libro
                    if 'subtitle' in book['volumeInfo']:
                        subtitle = book['volumeInfo']['subtitle']
                    else:
                        subtitle = ''

                    #Autor(es) del libro: lista[]
                    if 'authors' in book['volumeInfo']:
                        authors = book['volumeInfo']['authors']
                    else:
                        authors = ''

                    #Editorial del libro
                    if 'publisher' in book['volumeInfo']:
                        publisher = book['volumeInfo']['publisher']
                    else:
                        publisher = ''

                    #Fecha de publicación
                    if 'publishedDate' in book['volumeInfo']:
                        publishedDate = book['volumeInfo']['publishedDate']
                    else:
                        publishedDate = ''

                    #Breve descripcion
                    if 'description' in book['volumeInfo']:
                        description = book['volumeInfo']['description']
                    else:
                        description = ''

                    #ISBN (10)
                    if 'industryIdentifiers' in book['volumeInfo']:
                        isbn_10 = book['volumeInfo']['industryIdentifiers'][0]['identifier']
                    else:
                        isbn_10 = ''

                    #Número de paginas
                    if 'pageCount' in book['volumeInfo']:
                        numberPages = book['volumeInfo']['pageCount']
                    else:
                        numberPages = ''

                    #Categorias: lista[]
                    if 'categories' in book['volumeInfo']:
                        categories = book['volumeInfo']['categories']
                    else:
                        categories = ''

                    #Imagen de la portada
                    if 'imageLinks' in book['volumeInfo']:
                        if 'thumbnail' in book['volumeInfo']['imageLinks']:
                            image = book['volumeInfo']['imageLinks']['thumbnail']
                        else:
                            image = ''

                    #Link del libro
                    if 'previewLink' in book['volumeInfo']:
                        link = book['volumeInfo']['previewLink']
                    else:
                        link = ''

                    #Esta disponible en pdf (?): True | False
                    if 'accessInfo' in book:
                        if 'pdf' in book['accessInfo']:
                            if 'isAvailable' in book['accessInfo']['pdf']:
                                pdf = book['accessInfo']['pdf']['isAvailable']
                            else:
                                pdf = ''

                    #Solo se guardan los libros que contengan todos los datos, a excepción del subtitulo
                    if title!='' and authors !='' and publisher != '' and publishedDate != '' and description != '' and isbn_10 != '' and numberPages != '' and categories !='' and image != '' and link != '' and pdf != '':
                        #Aqui se crearan los objetos y se agregan a la lista de libros que va a regresar esta funcion
                        local_book = localBook(title, subtitle, authors, publisher, publishedDate, description, isbn_10, numberPages, categories, image, link, pdf)
                        list_books.append(local_book)


            return list_books


class APIServiceExtra(ABC):

    @abstractmethod
    def getExtras(self, word):
        pass
        """Regresa una lista de información extra que se obtiene de una nueva API.
        La clase que se conecta a la API implementa esta clase"""


if __name__ == '__main__':
    word = input("Search: ")
    #print(getBook(word))
    lista = APIConnection().getBook(word)
    for i in lista:
        print(i)
        #print(type(i))
        #if i.authors != None:print(", ".join(i.authors))
        #print(", ".join(i.authors) if i.authors !=None else i.authors)
        #print(", ".join(i.authors) if i.authors !='' else i.authors)
        #print(", ".join(i.categories) if i.categories !='' else i.categories)
        #print(type(i.pdf))
        #print(1 if i.pdf ==True else 0)
        #print(not None)
        #print(type(i))
        print('\n')

    sqlite = DataBase()
    #print(sqlite.SaveBook(lista[2]))
    #print(sqlite.ShowBook(lista[1]))
    #print(sqlite.DeleteBook(lista[2]))
