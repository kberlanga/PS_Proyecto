from abc import ABC, abstractmethod

class APIService(ABC):

    @abstractmethod
    def getBook(self, word):
        pass
        """Regresa una lista de objetos de tipo book. La clase que se conecta a la API implementa esta clase"""


class DBService(ABC):

    @abstractmethod
    def CreateTable(self):
        pass
        """Se hace la conexión a la base de datos y se crea la tabla 'books' """

    @abstractmethod
    def SaveBook(self, book_obj):
        pass
        """Se recibe un objeto de tipo Book (se obtiene el método <getBook()>), se obtiene la informacion correspondiente
        a la tabla y se guardan los datos en la base de datos"""

    @abstractmethod
    def DeleteBook(self, identifier):
        pass
        """Se recibe el identificador del libro que se eliminará de la base de datos"""

    @abstractmethod
    def UpdateBook(self, identifier):
    	pass

    @abstractmethod
    def ShowBook(self, identifier):
    	pass

    @abstractmethod
    def ShowAllBooks(self):
        pass


class Book(object):
    """ Objeto de tipo Book"""

    def __init__(self, title, subtitle, authors, publisher, publishedDate, description, isbn_10, numberPages, categories, image, link, pdf):
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

    def __str__(self):
        return """
        Title: {}\nSubtitle: {}\nAuthors: {}\nPublisher: {}\nPublished date: {}\nDescription: {}\nISBN: {}\nNumber Pages: {}\nCategories: {}\nImage: {}\nLink: {}\nPDF: {}
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
        self.pdf
        ).strip()



def main():
    pass


if __name__ == "__main__":
    main()
