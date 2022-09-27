from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos=0
    leones=0
    __listado=[]
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre,edad,habitat,genero)
        self.__pelaje=pelaje
        self.__patas=patas


#metodos sett

    @classmethod
    def setListado(cls, Mamifero):
        cls.__listado.append(Mamifero)

    def setPelaje(self, pelaje):
        self.__pelaje=pelaje

    def setPatas(self, patas):
        self.__patas=patas

#metodos gett

    @classmethod
    def getListado(cls):
        return cls.__listado
    
    def isPelaje(self):
        return self.__pelaje
    
    def getPatas(self):
        return self.__patas

#metodos de la clase

    @classmethod
    def cantidadMamiferos(cls):
        return len(cls.__listado)

    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon= Mamifero(nombre, edad, "selva", genero, True, 4)
        cls.__listado.append(leon)
        cls.leones +=1
        return leon
    
    
    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo= Mamifero(nombre, edad, "selva", genero, True, 4)
        cls.__listado.append(caballo)
        cls.caballos +=1
        return caballo

    