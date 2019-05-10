import unittest
import os
from unittest.mock import MagicMock
from interface_book import Book
from DataBase import DataBase, save, ShowBooks
import sqlite3

class TestInsert(unittest.TestCase):

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

        
    def tearDown(self):
        self.db.connection.close()
        os.remove("test_db_books.db")

    def testSaveBook(self):
        book = Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'], 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
        )
        entrada = book

        salida_esperada = Book(
        "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'], 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
        )

        # test_cases=(
        # (Book(
        # "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'], 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'),Book(
        # "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'], 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado')
        # ), (Book(
        # "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', None, 525, ['History'], 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'),"EL LIBRO I've Got the Light of Freedom YA EXISTE EN LA BASE DE DATOS")
        # )

        dbMock = MagicMock()
        dbMock.SaveBook.return_value = entrada
        real = save(dbMock, entrada)
        self.assertEqual(salida_esperada, real)

        # for entrada,salida_esperada in test_cases:
        #     dbMock = MagicMock()
        #     dbMock.SaveBook.return_value = entrada
        #     real = save(dbMock, entrada)
        #     self.assertEqual(salida_esperada, real)

# class TestShowAll(unittest.TestCase):
#
#     def setUp(self):
#         self.db = DataBase("test_db_books.db")
#         cursor = self.db.connection.cursor()
#         cursor.execute("""CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                                       isbn text,
#                                       title text,
#                                       subtitle text,
#                                       authors text,
#                                       publisher text,
#                                       published_date text,
#                                       description text,
#                                       number_pages int,
#                                       categories text,
#                                       image text,
#                                       link text,
#                                       pdf int,
#                                       weight real,
#                                       cost real
#                                 )""")
#         self.db.SaveBook(Book(
#         "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'], 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
#         ))
#
#
#     def tearDown(self):
#         self.db.connection.close()
#         os.remove("test_db_books.db")
#
#     def testShowAllBooks(self):
#         entrada = Book(
#         "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'], 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
#         )
#
#         salida_esperada = Book(
#         "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'], 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado'
#         )
#
#         dbMock = MagicMock()
#         dbMock.ShowAllBooks.return_value = entrada
#
#         real = ShowBooks(dbMock)
#         self.assertEqual(salida_esperada, real)
#
#
#     def testIntegrationShowAllBooks(self):
#         salida_esperada = [Book(
#         "I've Got the Light of Freedom", 'The Organizing Tradition and the Mississippi Freedom Struggle', ['Charles M. Payne'], 'Univ of California Press', '2007', '"With this history of the civil rights movement focusing on Everyman-turned-hero, the commoner as crusader for justice, Payne challenges the old idea that history is the biography of great men."--Kirkus Reviews "Remarkably astute in its judgments and strikingly sophisticated in its analyses . . . it is one of the most significant studies of the Black freedom struggle yet published."--David J. Garrow, author of the Pulitzer Prize-winning Bearing the Cross "This extremely important book clearly reveals the logic of how ordinary people propelled the civil rights movement. . . . [It] provides a basis for optimism as we approach the next century."--Aldon Morris, author of The Origins of the Civil Rights Movement', '0520251768', 525, ['History'], 'http://books.google.com/books/content?id=4eh_iGj2bzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api', 'http://books.google.com.mx/books?id=4eh_iGj2bzsC&pg=PR13&dq=got&hl=&cd=7&source=gbs_api', True ,'no identificado')]
#         real = ShowBooks(self.db)
#         self.assertEqual(salida_esperada, real)

if __name__ == "__main__":
    unittest.main()
