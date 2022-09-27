
class Zona:
    def __init__(self, nombre, zoo= None):
        self.__nombre= nombre
        self.__zoo= zoo
        self.__animales= []

   #metodos set 
    def setNombre(self,nombre):
        self.__nombre=nombre

    def setZoo(self,zoo):
        self.__zoo.append(zoo)
    
    def setAnimales(self, animales):
        self.__animales.append(animales)
   
    #metodos get
    def getNombre(self):
        return self.__nombre
    
    def getZoo(self):
        return self.__zoo
    
    def getAnimales(self):
        self.__animales
   
   #metodos de la clase 
    def cantidadAnimales(self):
        x= len(self.__animales)
        return x 
    
    def agregarAnimales(self, animales):
        self.__animales.append(animales)
        