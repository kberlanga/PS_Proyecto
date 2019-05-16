import sys
from APIConnectionGoogle import APIConnection, APIServiceExtra
from DataBase import DataBase

class Menu():
    def opcionesMenu(self):
        """Menú con las opciones a elegir"""
        print("\n- - - - - - - - - - MENÚ DE SELECCIÓN - - - - - - - - - -")
        print("1. Buscar libro y guardarlo en la base de datos")
        print("2. Buscar libro sin guardarlo aún en la base de datos")
        print("3. Ver libros guardados en la base de datos")
        print("4. Buscar un libro en específico en la base de datos")
        print("5. Actualizar el precio de algún libro")
        print("6. Borrar un libro de la base de datos")
        print("7. SALIR")
        print("¿Qué deseas hacer? Porfavor ingresa tu respuesta")

    def buscar_guardar_libro(self):
        """Método para buscar libro en la api y guardarlo inmediatamente en la base de datos"""
        # Pedimos el nombre del libro
        nombre = input("Porfavor, ingresa el nombre del libro: ")
        # Búsqueda en API
        lista = APIConnection().getBook(nombre, APIServiceExtra())
        # si la respuesta es none, no existe ese libro en la API, por lo tanto no se guarda en la base de datos
        if lista is None:
            print("No existen libros con ese nombre")
        else:
            # cuando si existe libro, se guarda en la base de datos
            for l in lista:
                print(l)
                respuesta = DataBase('db_books.db').SaveBook(l)
                print(respuesta)

    def buscar_libro(self):
        """Método para buscar un libro en la base de datos"""
        nombre = input("Porfavor, ingresa el nombre del libro: ")
        print(nombre) # pedimos el nombre del libro
        lista = APIConnection().getBook(nombre, APIServiceExtra())
        if lista is None:
            print("No existen libros con ese nombre")
        else:
            for l in lista:
                print(l)
                print('\n')

    def getDataBase(self):
        """Método para ver todos los libros almacenados en la base de datos"""
        lista_libros = DataBase('db_books.db').ShowAllBooks()
        for libro in lista_libros:
            print(libro)

    def getBookInDataBase(self):
        """Método para buscar un libro en específico de la base de datos"""
        isbn = input("Porfavor ingresa el ISBN: ")
        libro = DataBase('db_books.db').ShowBook(isbn)
        print(libro)

    def actualizar_precio(self):
        """Método para modificar el precio de algún libro en específico"""
        isbn = input("Porfavor ingresa el ISBN del libro:")
        precio = float(input("Porfavor ingresa el nuevo precio: "))
        respuesta = DataBase('db_books.db').UpdatePriceBook(isbn, precio)
        print(respuesta)

    def borrar_libro(self):
        """Método para borrar algún libro en específico"""
        isbn = input("Porfavor ingresa el ISBN del libro a borrar: ")
        # primero buscamos el libro en la base de datos por isbn
        libro = DataBase('db_books.db').ShowBook(isbn)
        # si el libro está en la base de datos, lo borramos
        if type(libro) == object:
            respuesta = DataBase('db_books.db').DeleteBook(libro)
            print(respuesta)
        # si el libro no está en la base de datos, el isbn proporcionado por el usuario es incorrecto
        else:
            print("ISBN incorrecto")


    def main(self):
        # Creamos la tabla de la base de datos donde guardaremos los libros
        DataBase('db_books.db').CreateTable()
        bool = True
        while True:
            self.opcionesMenu() # mostramos las opcines del menú
            try:
                opcion = int(input())
                bool = True
            except:
                # No se permiten ingresar valores distintos a números
                print("Ha ocurrido un error. Posible causa: Ingresaste un valor no numérico")
                bool = False

            if bool == True:
                if opcion <= 0 or opcion > 7: # no se puede ingresar valores distintos
                    print("Sólo se permiten valores del 1 al 7")
                elif opcion == 1:
                    self.buscar_guardar_libro()
                elif opcion == 2:
                    self.buscar_libro()
                elif opcion == 3:
                    self.getDataBase()
                elif opcion == 4:
                    self.getBookInDataBase()
                elif opcion == 5:
                    self.actualizar_precio()
                elif opcion == 6:
                    self.borrar_libro()
                else:
                    sys.exit("Hasta la próxima ;)") # Salida del programa


if __name__ == '__main__':
    Menu().main()
