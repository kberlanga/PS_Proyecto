from abc import ABC, abstractmethod

#Inteface
class APIService(ABC):

    @abstractmethod
    def GetPlant(self, plant_name):
        #Regresa un objeto de tipo Planta
        pass

#Interface
class DBService(ABC):

    @abstractmethod
    def SavePlant(self, plant_obj):
        pass

def AddPlant(api_service, db_service, name, favorite):

    if name[0].upper != name[0]:
        return 'nombre no válido'

    for letter in name:
        if l.isDigit():
            return 'nombre no válido'

    plant = api_service.GetPlant(name)
    plant.Favorite = favorite
    db_service.SavePlant(plant)

if __name__ == '__main__':
    pulpito = Pulpo('rojo')
    pulpito.mover()
    pulpito.respirar()

#Tarea
#La clase principal Libros con los atributos que va a tener (nombre, editorial, paginas) *campos que se extraen del API
#*y los datos extras que se van a agregar
#Las dos interfaces, la del api y la de la base de datos (las dos clases abstractas)
