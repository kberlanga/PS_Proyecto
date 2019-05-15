from interface_book import DBService, Book
import sqlite3

class DataBase(DBService):

    def __init__(self, file):
        self.connection = sqlite3.connect(file)

    def CreateTable(self):
        # Se crea la base de datos
        cursor = self.connection.cursor()
        try:
            # Se verifica que la tabla no exista. Se crea la tabla
            cursor.execute("""CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT,
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
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()
        # Se hace la siguiente consulta para verificar que el libro que se agregará no exista en la base de datos

        cursor.execute('''SELECT isbn FROM books WHERE isbn = "{}"'''.format(book.isbn_10))
        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        isbn = cursor.fetchone()

        if isbn is None:
            # Si el ibsn=None, se inserta el libro
            parametros = {
            'ISBN':book.isbn_10,
            'TITLE': book.title,
            'SUBTITLE':book.subtitle,
            'AUTHORS': ", ".join(book.authors) if book.authors !='' else book.authors,
            'PUBLISHER': book.publisher,
            'DATE':book.publishedDate,
            'DESCRIPTION': book.description,
            'PAGES':book.numberPages,
            'CATEGORIES': ", ".join(book.categories) if book.categories !='' else book.categories,
            'IMAGE': book.image,
            'LINK': book.link,
            'PDF': 1 if book.pdf == True else 0,
            'WEIGHT': book.weight,
            'COST': book.numberPages*.70}
            try:
                cursor.execute( "INSERT INTO books (id, isbn, title, subtitle, authors, publisher, published_date, description, number_pages, categories, image, link, pdf, weight, cost) VALUES(null,:ISBN,:TITLE,:SUBTITLE,:AUTHORS,:PUBLISHER,:DATE,:DESCRIPTION,:PAGES,:CATEGORIES,:IMAGE,:LINK,:PDF,:WEIGHT,:COST);", parametros)
                print("EL LIBRO {} SE INSERTÓ EXITOSAMENTE A LA BASE DE DATOS".format(book.title))

            except:
                return("ERROR AL INSERTAR EL LIBRO A LA BASE DE DATOS")

            self.connection.commit()
            cursor.execute("""SELECT * FROM books WHERE title = :TITLE """, {'TITLE': book.title})
            consulta = cursor.fetchall()
            list_books = []
            for libro in consulta:
                au = libro[4].split(",")
                cat = libro[9].split(",")
                for i in range(len(au)):
                    au[i]= au[i].strip()
                for j in range(len(cat)):
                    cat[j]= cat[j].strip()

                book = Book(libro[2], libro[3], au, libro[5], libro[6], libro[7], libro[1], libro[8], cat, libro[10], libro[11], libro[12], libro[13])
                list_books.append(book)
            return list_books
            self.connection.commit()
            #self.connection.close()
        else:
            #self.connection.close()
            return "EL LIBRO {} YA EXISTE EN LA BASE DE DATOS".format(book.title)

    def DeleteBook(self, book):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()

        # Se verifica que el libro que se recibe contenga datos
        if not book:
            # Si el libro esta vacío, se devuelve un mensaje
            return "NO SE PUEDE ELIMINAR EL LIBRO. NO EXISTE EN LA BASE DE DATOS"
        else:
            # De manera contraria se hace una consulta a la base de datos del libro
            cursor.execute("""SELECT * FROM books WHERE isbn = '{}'""".format(book.isbn_10))
            registros = cursor.fetchall()
            # Se revisa que la consulta regrese algun registro
            if registros == []: # Si no es así, se regresa un mensaje
                return "NO SE PUEDE ELIMINAR EL LIBRO. NO EXISTE EN LA BASE DE DATOS"

            # Se procede a eliminar el libro indicado
            list_books = []
            cursor.execute("""DELETE FROM books WHERE isbn = {}""".format(book.isbn_10))
            self.connection.commit()
            cursor.execute("""SELECT * FROM books WHERE isbn = {}""".format(book.isbn_10))
            consulta = cursor.fetchall()
            for libro in consulta:
                au = libro[4].split(",")
                cat = libro[9].split(",")
                for i in range(len(au)):
                    au[i]= au[i].strip()
                for j in range(len(cat)):
                    cat[j]= cat[j].strip()
                book = Book(libro[2], libro[3], au, libro[5], libro[6], libro[7], libro[1], libro[8], cat, libro[10], libro[11], libro[12], libro[13])
                list_books.append(book)
            #Se puede o no regresar el libro

            return("""SE HA ELIMINADO DE MANERA CORRECTA EL LIBRO {}""".format(book.title))

    def UpdatePriceBook(self, isbn, precio):
        # Se hace la conexión a la base de datos
        cursor = self.connection.cursor()

        cursor.execute('''SELECT isbn FROM books WHERE isbn = "{}"'''.format(isbn))
        # Se guarda el resultado de la consulta anterior en la variable isbn, puede contener un isbn o None
        isbn_10 = cursor.fetchone()

        # Se verifica que el libro que se recibe contenga datos
        if isbn_10 == None:
            # Si el libro esta vacío, se devuelve un mensaje
            return "NO SE PUEDE ACTUALIZAR EL LIBRO. NO EXISTE EN LA BASE DE DATOS"
        else:
            # De manera contraria se actualiza
            cursor.execute("""UPDATE books set cost={} where isbn='{}'""".format(precio, isbn))
            registros = cursor.fetchall()
            self.connection.commit()
            #self.connection.close()

            return "SE HA ACTUALIZADO EL PRECIO DEL LIBRO CORRECTAMENTE"

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

        au = consulta[0][4].split(",")
        cat = consulta[0][9].split(",")
        for i in range(len(au)):
            au[i]= au[i].strip()
        for j in range(len(cat)):
            cat[j]= cat[j].strip()

        book = Book(consulta[0][2], consulta[0][3], au, consulta[0][5], consulta[0][6], consulta[0][7], consulta[0][1], consulta[0][8], cat, consulta[0][10], consulta[0][11], consulta[0][12], consulta[0][13])
        self.connection.commit()
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
            au = libro[4].split(",")
            cat = libro[9].split(",")
            for i in range(len(au)):
                au[i]= au[i].strip()
            for j in range(len(cat)):
                cat[j]= cat[j].strip()
            book = Book(libro[2], libro[3], au, libro[5], libro[6], libro[7], libro[1], libro[8], cat, libro[10], libro[11], libro[12], libro[13])
            list_books.append(book)
        return list_books



#--------------------------------------------------------------------------------------------#
def save(db, book):
    r = db.SaveBook(book)
    return r

def showBooks(db):
    books = db.ShowAllBooks()
    return books

def show(db,isbn):
    book = db.ShowBook(isbn)
    return book

def delete(db, book):
    msg = db.DeleteBook(book)
    return msg

def update(db, isbn, precio):
    msg = db.UpdatePriceBook(isbn, precio)
    return msg




if __name__ == '__main__':
    #print(DataBase().ShowBook('1859846661'))
    db = DataBase("db_books.db")
    # lista = ShowBooks(db)
    # for libro in lista:
    #     print(libro)
    #print(*showBooks(db), sep="\n")
    lista = showBooks(db)
    print(lista)
    #for book in lista:
        #print(book)
    #print(Show(db,'0520251768'))
    #print
    #print(lista[72])
    # book = Book(
    # ["I've Got the Light of Freedom"], 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0625251785', 525, ['History'],
    # 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
    # )
    # #print(delete(db, book))
    # print(save(db, book))

    #DataBase().DeleteBook(lista[len(lista)-1])
    #print(lista[67])
    pass
