from interface_book import DBService, Book
import sqlite3

class DataBase(DBService):

    def __init__(self):
        self.connection = sqlite3.connect("db_books.db")

    def CreateTable(self):
        # Se crea la base de datos
        cursor = self.connection.cursor()
        try:
            # Se verifica que la tabla no exista. Se crea la tabla
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
        # Se verifica el resultado de la consulta
        if type(book) is str: # Si es un string, quiere decir que la solicitud a la API falló
            return "ERROR AL AGREGAR EL LIBRO A LA TABLA. VERIFIQUE QUE EL NOMBRE DEL LIBRO ESTÉ CORRECTO"

        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()
        # Se hace la siguiente consulta para verificar que el libro que se agregará no exista en la base de datos

        cursor.execute('''SELECT isbn FROM books WHERE isbn = "{}"'''.format(book.isbn_10))
        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        isbn = cursor.fetchone()

        if isbn is None:
            # Si el ibsn=None, se inserta el libro
            parametros = (
            book.isbn_10, book.title,
            book.subtitle,
            ", ".join(book.authors) if book.authors !='' else book.authors, book.publisher, book.publishedDate,
            book.description, book.numberPages, ", ".join(book.categories) if book.categories !='' else book.categories,
            book.image, book.link, 1 if book.pdf == True else 0, book.weight, book.numberPages*.70)
            if cursor.execute( """INSERT INTO books VALUES(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", parametros):
                print("EL LIBRO {} SE INSERTÓ EXITOSAMENTE A LA BASE DE DATOS".format(book.title))

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
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()

        # Se verifica que el libro que se recibe contenga datos
        if book == None:
            # Si el libro esta vacío, se devuelve un mensaje
            return "NO SE PUEDE ELIMINAR EL LIBRO, YA QUE NO EXISTE EN LA BASE DE DATOS"
        else:
            # De manera contraria se hace una consulta a la base de datos del libro
            cursor.execute("""SELECT * FROM books WHERE isbn = {}""".format(book.isbn_10))
            registros = cursor.fetchall()
            # Se revisa que la consulta regrese algun registro
            if registros == []: # Si no es así, se regresa un mensaje
                return "NO SE PUEDE ELIMINAR EL LIBRO, ÉSTE NO EXISTE EN LA BASE DE DATOS"

            # Se procede a eliminar el libro indicado
            cursor.execute("""DELETE FROM books WHERE isbn = {}""".format(book.isbn_10))
            self.connection.commit()

            cursor.execute("""SELECT * FROM books WHERE isbn = {}""".format(book.isbn_10))
            consulta = cursor.fetchall()
            print("""SE HA ELIMINADO DE MANERA CORRECTA EL LIBRO {}""".format(book.title))
            return consulta

            self.connection.commit()
            self.connection.close()

    def UpdatePriceBook(self, isbn, precio):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()

        cursor.execute('''SELECT isbn FROM books WHERE isbn = "{}"'''.format(isbn))
        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        isbn_10 = cursor.fetchone()

        # Se verifica que el libro que se recibe contenga datos
        if isbn_10 == None:
            # Si el libro esta vacío, se devuelve un mensaje
            return "NO SE PUEDE ACTUALIZAR EL LIBRO, YA QUE NO EXISTE EN LA BASE DE DATOS"
        else:
            # De manera contraria se actualiza
            cursor.execute("""UPDATE books set cost={} where isbn='{}'""".format(precio, isbn))
            registros = cursor.fetchall()
            self.connection.commit()
            self.connection.close()

            return "Se ha actualizado el precio correctamente"

    def ShowBook(self, isbn):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()

        cursor.execute('''SELECT isbn FROM books WHERE isbn = "{}"'''.format(isbn))
        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        isbn_10 = cursor.fetchone()

        # Se verifica que el libro que se recibe contenga datos
        if isbn_10 == None:
            # Si el libro esta vacío, se devuelve un mensaje
            return "EL LIBRO BUSCADO NO SE ENCUENTRA EN LA BASE DE DATOS"

        cursor.execute("""SELECT * FROM books WHERE isbn = '{}'""".format(isbn))
        consulta = cursor.fetchall()
        #book = Book()
        book = Book(consulta[0][2], consulta[0][3], consulta[0][4], consulta[0][5], consulta[0][6], consulta[0][7], consulta[0][1], consulta[0][8], consulta[0][9], consulta[0][10], consulta[0][11], consulta[0][12], consulta[0][13])
        self.connection.commit()
        self.connection.close()
        return book




    def ShowAllBooks(self):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()
        list_books = []

        # Se hace la consulta de los libros que se mostrará para ver si hay registros
        cursor.execute("""SELECT * FROM books""")
        registros = cursor.fetchall()
        if registros == []:
            return "NO HAY REGISTROS EN LA BASE DE DATOS"

        cursor.execute("""SELECT * FROM books""")
        consulta = cursor.fetchall()
        for libro in consulta:
            book = Book(libro[2], libro[3], libro[4], libro[5], libro[6], libro[7], libro[1], libro[8], libro[9], libro[10], libro[11], libro[12], libro[13])
            list_books.append(book)
        self.connection.commit()
        self.connection.close()
        return list_books






if __name__ == '__main__':
    #print(DataBase().ShowBook('1859846661'))
    #lista = DataBase().ShowAllBooks()
    #for libro in lista:
    #    print(libro)

    #DataBase().DeleteBook(lista[len(lista)-1])
    #print(lista[67])
    pass
