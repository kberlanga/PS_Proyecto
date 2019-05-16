import unittest
import os
from unittest.mock import MagicMock
from interface_book import Book
from DataBase import DataBase, save, showBooks, show, delete, update
import sqlite3

class TestDataBase(unittest.TestCase):

    def setUp(self):
        self.db = DataBase("test_db_books.db")
        cursor = self.db.connection.cursor()
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
        self.db.SaveBook(Book(
                 "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
                 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
                 ))
        self.db.SaveBook(Book(
        "Jo", 'Art of the Japanese Short Staff', ['Dave Lowry', 'Mike Lee'], 'Black Belt Communications', '1987', 'The jo appears to be the lowliest of all tools--an ordinary length of wood--yet it’s an exceptional weapon. While no one speaks of famous jo makers the way they do of sword smiths, the jo is capable of snapping the best swords ever forged. Packed with information on correct grips, stances, postures and etiquette, the book also outlines striking methods, combination techniques, and a 31-count formal solo exercise called tandoku renshu, making it the ultimate resource for those who appreciate Japan’s most subtle weapon.', '191', 525, ['Sports & Recreation'], 'http://books.google.com/books/content?id=57sOo2TpPYUC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=57sOo2TpPYUC&printsec=frontcover&dq=JO&hl=&cd=6&source=gbs_api', False ,'9.1 ounces'))



    def tearDown(self):
        self.db.connection.close()
        os.remove("test_db_books.db")

#------------------------------------------------TEST SAVE-----------------------------------------------------------------------------------------#


    def testSaveBook(self):

        test_cases=(
        ([Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado')],Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado')
        ),
        (Book(
        ["I've Got the Light of Freedom"], 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'), "ERROR AL INSERTAR EL LIBRO A LA BASE DE DATOS"),
        (Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', None, 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'),"EL LIBRO I've Got the Light of Freedom YA EXISTE EN LA BASE DE DATOS")
        )


        for entrada,salida_esperada in test_cases:
            dbMock = MagicMock()
            dbMock.SaveBook.return_value = salida_esperada
            real = save(dbMock, entrada)
            self.assertEqual(salida_esperada, real)

    def testIntegrationSave(self):
        #Test Cases: (salida_esperada, objeto a guardar)
        test_cases=(
        ([Book(
        "El principito", 'Art of the Japanese Short Staff', ['Dave Lowry', 'Mike Lee'], 'Black Belt Communications', '1987', 'The jo appears to be the lowliest of all tools--an ordinary length of wood--yet it’s an exceptional weapon. While no one speaks of famous jo makers the way they do of sword smiths, the jo is capable of snapping the best swords ever forged. Packed with information on correct grips, stances, postures and etiquette, the book also outlines striking methods, combination techniques, and a 31-count formal solo exercise called tandoku renshu, making it the ultimate resource for those who appreciate Japan’s most subtle weapon.', '192', 525, ['Sports & Recreation'], 'http://books.google.com/books/content?id=57sOo2TpPYUC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=57sOo2TpPYUC&printsec=frontcover&dq=JO&hl=&cd=6&source=gbs_api', False ,'9.1 ounces')], Book(
        "El principito", 'Art of the Japanese Short Staff', ['Dave Lowry', 'Mike Lee'], 'Black Belt Communications', '1987', 'The jo appears to be the lowliest of all tools--an ordinary length of wood--yet it’s an exceptional weapon. While no one speaks of famous jo makers the way they do of sword smiths, the jo is capable of snapping the best swords ever forged. Packed with information on correct grips, stances, postures and etiquette, the book also outlines striking methods, combination techniques, and a 31-count formal solo exercise called tandoku renshu, making it the ultimate resource for those who appreciate Japan’s most subtle weapon.', '192', 525, ['Sports & Recreation'], 'http://books.google.com/books/content?id=57sOo2TpPYUC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=57sOo2TpPYUC&printsec=frontcover&dq=JO&hl=&cd=6&source=gbs_api', False ,'9.1 ounces')),
        ("EL LIBRO I've Got the Light of Freedom YA EXISTE EN LA BASE DE DATOS", Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado')
        ),
        ("ERROR AL INSERTAR EL LIBRO A LA BASE DE DATOS",Book(
        ["I've Got the Light of Freedom"], 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0625251785', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
        ))
        )

        for esperada, book in test_cases:
            salida_esperada = esperada
            real = save(self.db, book)
            self.assertEqual(salida_esperada, real)

#------------------------------------------------TEST SHOW_ALL-----------------------------------------------------------------------------------------#


    def testShowAllBooks(self):
        entrada = Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
        )

        salida_esperada = [Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
        )]

        dbMock = MagicMock()
        dbMock.ShowAllBooks.return_value = salida_esperada

        real = showBooks(dbMock)
        self.assertEqual(salida_esperada, real)


    def testIntegrationShowAllBooks(self):
        #Como hacer para la prueba en la que no hay elementos en la base de datos
        #si se tiene que insertar en la base de datos para uno de los casos
        salida_esperada = [Book("I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'),Book("Jo", 'Art of the Japanese Short Staff', ['Dave Lowry', 'Mike Lee'], 'Black Belt Communications', '1987', 'The jo appears to be the lowliest of all tools--an ordinary length of wood--yet it’s an exceptional weapon. While no one speaks of famous jo makers the way they do of sword smiths, the jo is capable of snapping the best swords ever forged. Packed with information on correct grips, stances, postures and etiquette, the book also outlines striking methods, combination techniques, and a 31-count formal solo exercise called tandoku renshu, making it the ultimate resource for those who appreciate Japan’s most subtle weapon.', '191', 525, ['Sports & Recreation'],
        'http://books.google.com/books/content?id=57sOo2TpPYUC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=57sOo2TpPYUC&printsec=frontcover&dq=JO&hl=&cd=6&source=gbs_api', False ,'9.1 ounces')]
        real = showBooks(self.db)
        self.assertEqual(salida_esperada, real)

#------------------------------------------------TEST SHOW-----------------------------------------------------------------------------------------#

    def testShowBook(self):
        #entrada, salida_esperada
        test_cases=(
        ('0520251768',Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
        )),
        ('0580251768',"EL LIBRO BUSCADO NO SE ENCUENTRA EN LA BASE DE DATOS" )
        )


        dbMock = MagicMock()
        for entrada, salida_esperada in test_cases:
         dbMock.ShowBook.return_value = salida_esperada
         dbMock.isbn_10.return_value = None
         real = show(dbMock, entrada)
         self.assertEqual(salida_esperada, real)


    def testIntegrationShowBook(self):
        #entrada, salida_esperada
        test_cases=(
        ('0520251768',Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado')
        ),
        ('0580251768',"EL LIBRO BUSCADO NO SE ENCUENTRA EN LA BASE DE DATOS")
        )
        for entrada, salida_esperada in test_cases:
         real = show(self.db,entrada)
         self.assertEqual(salida_esperada, real)

#------------------------------------------------TEST UPDATE-----------------------------------------------------------------------------------------#

    def testUpdateBook(self):
        test_cases=(
        ('0520251768',25.50,"SE HA ACTUALIZADO EL PRECIO DEL LIBRO CORRECTAMENTE"),
        ('1680671759',26.50, "NO SE PUEDE ACTUALIZAR EL LIBRO. NO EXISTE EN LA BASE DE DATOS")
        )

        for isbn, precio, salida_esperada in test_cases:
         dbMock = MagicMock()
         dbMock.UpdatePriceBook.return_value = salida_esperada
         real = update(dbMock, isbn, precio)
         self.assertEqual(salida_esperada, real)


    def testIntegrationUpdateBook(self):
        test_cases=(
        ('0520251768',25.50,"SE HA ACTUALIZADO EL PRECIO DEL LIBRO CORRECTAMENTE"),
        ('1680671759',26.50, "NO SE PUEDE ACTUALIZAR EL LIBRO. NO EXISTE EN LA BASE DE DATOS")
        )
        for isbn,precio, salida_esperada in test_cases:
          real = update(self.db, isbn, precio)
          self.assertEqual(salida_esperada, real)

#------------------------------------------------TEST DELETE-----------------------------------------------------------------------------------------#

    def testDeleteBook(self):
        test_cases=(
        (Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
        ),"SE HA ELIMINADO DE MANERA CORRECTA EL LIBRO I've Got the Light of Freedom"),
        (None,"NO SE PUEDE ELIMINAR EL LIBRO. NO EXISTE EN LA BASE DE DATOS"),
        (Book(
        "Jo", 'Art of the Japanese Short Staff', ['Dave Lowry', 'Mike Lee'], 'Black Belt Communications', '1987', 'The jo appears to be the lowliest of all tools--an ordinary length of wood--yet it’s an exceptional weapon. While no one speaks of famous jo makers the way they do of sword smiths, the jo is capable of snapping the best swords ever forged. Packed with information on correct grips, stances, postures and etiquette, the book also outlines striking methods, combination techniques, and a 31-count formal solo exercise called tandoku renshu, making it the ultimate resource for those who appreciate Japan’s most subtle weapon.', '191', 525, ['Sports & Recreation'], 'http://books.google.com/books/content?id=57sOo2TpPYUC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=57sOo2TpPYUC&printsec=frontcover&dq=JO&hl=&cd=6&source=gbs_api', False ,'9.1 ounces'), "NO SE PUEDE ELIMINAR EL LIBRO. NO EXISTE EN LA BASE DE DATOS")
        )

        for entrada, salida_esperada in test_cases:
         dbMock = MagicMock()
         dbMock.DeleteBook.return_value = salida_esperada
         real = delete(dbMock, entrada)
         self.assertEqual(salida_esperada, real)


    def testIntegrationDeleteBook(self):
        test_cases = (
        (Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'],
        'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'),
        "SE HA ELIMINADO DE MANERA CORRECTA EL LIBRO I've Got the Light of Freedom"),
        (None,"NO SE PUEDE ELIMINAR EL LIBRO. NO EXISTE EN LA BASE DE DATOS"),
        (Book("El principito", 'Art of the Japanese Short Staff', ['Dave Lowry', 'Mike Lee'], 'Black Belt Communications', '1987', 'The jo appears to be the lowliest of all tools--an ordinary length of wood--yet it’s an exceptional weapon. While no one speaks of famous jo makers the way they do of sword smiths, the jo is capable of snapping the best swords ever forged. Packed with information on correct grips, stances, postures and etiquette, the book also outlines striking methods, combination techniques, and a 31-count formal solo exercise called tandoku renshu, making it the ultimate resource for those who appreciate Japan’s most subtle weapon.', '192', 525, ['Sports & Recreation'], 'http://books.google.com/books/content?id=57sOo2TpPYUC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=57sOo2TpPYUC&printsec=frontcover&dq=JO&hl=&cd=6&source=gbs_api', False ,'9.1 ounces'),
        "NO SE PUEDE ELIMINAR EL LIBRO. NO EXISTE EN LA BASE DE DATOS")
        )
        for entrada, salida_esperada in test_cases:
          real = delete(self.db, entrada)
          self.assertEqual(salida_esperada, real)

if __name__ == "__main__":
    unittest.main()
