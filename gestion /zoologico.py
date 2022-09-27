class Zoologico:
    __zonas=[]
    def __init__(self, nombre, ubicacion):
        self.__nombre= nombre 
        self.__ubicacion= ubicacion
    
    #metodos sett

    def setNombre(self, nombre):
        self.__nombre=nombre
    
    def setUbicacion(self, ubicacion):
        self.__ubicacion=ubicacion
   
    def setZonas(self, zonas):
        self.__zonas.append(zonas)

    #metodos gett
    def getNombre(self):
        return self.__nombre

    def getUbiacion(self):
        return self.__ubicacion
    
    def getZona(self):
        return self.__zonas

    #metodos de la clase

    def agregarZonas(self, zonas):
        self.__zonas.append(zonas)

    def cantidadTotalAnimales(self):
        e= 0
        total= 0
        while e< len(self.__zonas):
            e +=1
            total += self.__zonas[e].cantidadAnimales()
        return total


