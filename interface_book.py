from abc import ABC, abstractmethod

class APIService(ABC):

    @abstractmethod
    def getBook(self, word, serviceEx):
        pass
        """Regresa una lista de objetos de tipo book. La clase que se conecta a la API implementa esta clase"""

class APIServiceExtra(ABC):

    @abstractmethod
    def getExtras(self, isbn):
        pass
        """Regresa una lista de información extra que se obtiene de una nueva API.
        La clase que se conecta a la API implementa esta clase"""


class DBService(ABC):

    @abstractmethod
    def CreateTable(self):
        pass
        """Se hace la conexión a la base de datos y se crea la tabla 'books' """

    @abstractmethod
    def SaveBook(self, book_obj):
        pass
        """Se recibe un objeto de tipo Book (se obtiene el método <getBook()>), se obtiene la información correspondiente
        a la tabla y se guardan los datos en la base de datos"""

    @abstractmethod
    def DeleteBook(self, identifier):
        pass
        """Se recibe el identificador del libro que se eliminará de la base de datos"""

    @abstractmethod
    def UpdatePriceBook(self, identifier, price):
    	pass

    @abstractmethod
    def ShowBook(self, identifier):
    	pass

    @abstractmethod
    def ShowAllBooks(self):
        pass


class Book(object):
    """ Objeto de tipo Book"""

    def __init__(self, title, subtitle, authors, publisher, publishedDate, description, isbn_10, numberPages, categories, image, link, pdf, weight):
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.publisher = publisher
        self.publishedDate = publishedDate
        self.description = description
        self.isbn_10 = isbn_10
        self.numberPages = numberPages
        self.categories = categories
        self.image = image
        self.link = link
        self.pdf = pdf
        self.weight = weight
        self.price = self.numberPages * .70

    def __str__(self):
        return """
        - Title: {}\n - Subtitle: {}\n - Authors: {}\n - Publisher: {}\n - Published date: {}\n - Description: {}\n - ISBN: {}\n - Number Pages: {}\n - Categories: {}\n - Image: {}\n - Link: {}\n - PDF: {}\n - Weight: {}\n - Precio: {}
        """.format(
        self.title,
        self.subtitle,
        self.authors,
        self.publisher,
        self.publishedDate,
        self.description,
        self.isbn_10,
        self.numberPages,
        self.categories,
        self.image,
        self.link,
        self.pdf,
        self.weight,
        self.price
        ).strip()


def main():
    pass


if __name__ == "__main__":
    main()
