from zooAnimales.animal import  Animal

class Anfibio(Animal):
    salamandras=0
    ranas=0
    __listado=list()
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorPiel=colorPiel
        self.__venenoso=venenoso

#metodos sett

    def setColorPiel(self, colorPiel):
        self.__colorPiel=colorPiel

    def setVenenoso(self, venenoso):
        self.__venenoso=venenoso
    
    @classmethod
    def setListado(cls, Anfibio):
        cls.__listado.append(Anfibio)

#metodos gett

    def getColorPiel(self):
        return self.__colorPiel

    def isVenenoso(self):
        return self.__venenoso
    
    @classmethod
    def getListado(cls):
        return cls.__listado

#metodos de la clase 


    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana= Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas +=1
        cls.__listado.append(rana)
        return rana
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.__listado)

    def movimiento(self):
        x= "saltar"
        return x

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra= Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.__listado.append(salamandra)
        cls.salamandras +=1
        return salamandra