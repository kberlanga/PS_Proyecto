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


    def __eq__(self, book):
        if book.title != self.title:
            print(book.title, "es diferente a", self.title)
            return False

        if book.subtitle != self.subtitle:
            print(book.subtitle, "es diferente a", self.subtitle)
            return False

        if book.authors != self.authors:
            print(book.authors, "es diferente a", self.authors)
            return False

        if book.publisher != self.publisher:
            print(book.publisher, "es diferente a", self.publisher)
            return False

        if book.publishedDate != self.publishedDate:
            print(book.publishedDate, "es diferente a", self.publishedDate)
            return False

        if book.description != self.description:
            print(book.description, "es diferente a", self.description)
            return False

        if book.isbn_10 != self.isbn_10:
            print(book.isbn_10, "es diferente a", self.isbn_10)
            return False

        if book.numberPages != self.numberPages:
            print(book.numberPages, "es diferente a", self.numberPages)
            return False

        if book.categories != self.categories:
            print(book.categories, "es diferente a", self.categories)
            return False

        if book.image != self.image:
            print(book.image, "es diferente a", self.image)
            return False

        if book.link != self.link:
            print(book.link, "es diferente a", self.link)
            return False

        if book.pdf != self.pdf:
            print(book.pdf, "es diferente a", self.pdf)
            return False

        if book.weight != self.weight:
            print(book.weight, "es diferente a", self.weight)
            return False

        if book.price != self.price:
            print(book.price, "es diferente a", self.price)
            return False

        return True


def main():
    pass


if __name__ == "__main__":
    main()
