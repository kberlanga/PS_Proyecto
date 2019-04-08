from interface_book import DBService
import sqlite3

class DataBase(DBService):

    def __init__(self):
        self.connection = sqlite3.connect("db_books.db")

    def CreateTable(self):
        #Se crea la base de datos
        ##connection = sqlite3.connect("db_books.db")
        cursor = self.connection.cursor()
        try:
            #Se verifica que la tabla no exista. Se crea la tabla
            self.connection.execute("""CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                      isbn text,
                                      title text,
                                      subtitle text,
                                      authors text,
                                      publisher text,
                                      published_date text,
                                      description text,
                                      number_pages int,
                                      categories text,
                                      image text,
                                      link text,
                                      pdf int,
                                      weight real,
                                      cost real
                                )""")
            return ("LA TABLA book SE CREÓ EXITOSAMENTE")
        except sqlite3.OperationalError:
            return ("OCURRIÓ UN ERROR")

        self.connection.commit()
        self.connection.close()

    def SaveBook(self, book):
        #Se verifica el resultado de la consulta
        if type(book) is str: #Si es un string, quiere decir que la solicitud a la API falló
            return "ERROR AL AGREGAR EL LIBRO A LA TABLA. VERIFIQUE QUE EL NOMBRE DEL LIBRO ESTE CORRECTO"

        #Se hace la conexión a la base de datos
        ##self.connection = sqlite3.connect("db_books.db")
        cursor = self.connection.cursor()
        #Se hace la siguiente consulta para verificar que el libro que se agregará no exista en la base de datos
        #cursor.execute('''SELECT ibsn FROM books WHERE ibsn = :ISBN''', {'IBSN': book.isbn_10})
        cursor.execute('''SELECT isbn FROM books WHERE isbn ={}'''.format(book.isbn_10))
        #Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        isbn = cursor.fetchone()
        if not isbn:
            #Si el ibsn=None, se inserta el libro
            parametros = (
            book.isbn_10, book.title,
            book.subtitle,
            ", ".join(book.authors) if book.authors !='' else book.authors, book.publisher, book.publishedDate,
            book.description, book.numberPages, ", ".join(book.categories) if book.categories !='' else book.categories,
            book.image, book.link, 1 if book.pdf == True else 0, 0, 0)
            if cursor.execute( """INSERT INTO books VALUES(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", parametros):
                print("EL LIBRO {} SE INSERTÓ EXITOSAMENTE A LA BASE DE DATOS".format(book.title))
            #if cursor.execute("""INSERT INTO books VALUES(
            #:ID, :IBSN, :TITLE, :SUBTITLE, :AUTHORS, :PUBLISHER, :PUBLISHED_DATE,
            #:DESCRIPTION, :NUMBER_PAGES, :CATEGORIES, :IMAGE, :LINK, :PDF, :WEIGHT, :COST)""",{
            #"ISBN":book.isbn_10,
            #"TITLE": book.title,
            #"SUBTITLE": book.subtitle,
            #"AUTHORS": ", ".join(book.authors) if book.authors !='' else book.authors,
            #"PUBLISHER": book.publisher,
            #"PUBLISHED_DATE": book.publishedDate,
            #"DESCRIPTION": book.description,
            #"NUMBER_PAGES": book.numberPages,
            #"CATEGORIES": ", ".join(book.categories) if book.categories !='' else book.categories,
            #"IMAGE": book.image,
            #"LINK": book.link,
            #"PDF": 1 if book.pdf == True else 0,
            #"WEIGHT": 0,
            #"COST": 0}):
            #    self.connection.commit()
            #    print("EL LIBRO {} SE INSERTÓ EXITOSAMENTE A LA BASE DE DATOS".format(book.title))

            else:
                print("ERROR AL INSERTAR EL LIBRO A LA BASE DE DATOS")
            self.connection.commit()
            cursor.execute("""SELECT * FROM books WHERE title = :TITLE """, {'TITLE': book.title})
            return cursor.fetchall()
            self.connection.close()
        else:
            self.connection.close()
            return "EL LIBRO {} YA EXISTE EN LA BASE DE DATOS".format(book.title)


    def DeleteBook(self, book):
        #Se hace la conexión a la base de datos
        ##self.connection = sqlite3.connect("db_books.db")
        cursor = self.connection.cursor()

        #Se verifica que el libro que se recibe contenga datos
        if book == None:
            #Si el libro esta vacío, se devuelve un mensaje
            return "NO SE PUEDE ELIMINAR EL LIBRO, YA QUE NO EXISTE EN LA BASE DE DATOS"
        else:
            #De manera contraria se hace una consulta a la base de datos del libro
            cursor.execute("""SELECT * FROM books WHERE isbn = {}""".format(book.isbn_10))
            registros = cursor.fetchall()
            #Se revisa que la consulta regrese algun registro
            if registros == []: #Si no es así, se regresa un mensaje
                return "NO SE PUEDE ELIMINAR EL LIBRO, ÉSTE NO EXISTE EN LA BASE DE DATOS"

            #Se procede a eliminar el libro indicado
            cursor.execute("""DELETE FROM books WHERE isbn = {}""".format(book.isbn_10))
            self.connection.commit()

            cursor.execute("""SELECT * FROM books WHERE isbn = {}""".format(book.isbn_10))
            consulta = cursor.fetchall()
            print("""SE HA ELIMINADO DE MANERA CORRECTA EL LIBRO {}""".format(book.title))
            return consulta

            self.connection.commit()
            self.connection.close()




    def UpdateBook(self, book):
        return 'Hola'

    def ShowBook(self, book):
        #Se hace la conexión a la base de datos
        ##self.connection = sqlite3.connect("db_books.db")
        cursor = self.connection.cursor()

        #Se verifica que el libro que se recibe contenga datos
        if book == None:
            #Si el libro esta vacío, se devuelve un mensaje
            return "EL LIBRO BUSCADO NO SE ENCUENTRA EN LA BASE DE DATOS"

        #Se hace la consulta del libro que se mostrará para ver si hay algun registro de éste
        cursor.execute("""SELECT * FROM books WHERE isbn = :ISBN""", {'ISBN': book.isbn_10})
        registros = cursor.fetchall()
        if registros == []:
            return "EL LIBRO QUE BUSCAS NO SE ENCUENTRA EN LA BASE DE DATOS"

        cursor.execute("""SELECT * FROM books WHERE isbn = :ISBN""", {'ISBN': book.isbn_10})
        consulta = cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return consulta




    def ShowAllBooks(self):
        #Se hace la conexión a la base de datos
        ##self.connection = sqlite3.connect("db_books.db")
        cursor = self.connection.cursor()

        #Se hace la consulta de los libros que se mostrará para ver si hay registros
        cursor.execute("""SELECT * FROM books""")
        registros = cursor.fetchall()
        if registros == []:
            return "NO HAY REGISTROS EN LA BASE DE DATOS"

        cursor.execute("""SELECT * FROM books""")
        consulta = cursor.fetchall()
        self.connection.commit()
        self.connection.close()
        return consulta






if __name__ == '__main__':
    #mensaje = DataBase().CreateTable()
    #print(mensaje)
    for book in DataBase().ShowAllBooks():
        print(book, '\n')
    pass
