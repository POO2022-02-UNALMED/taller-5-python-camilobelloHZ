from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil

class Animal:
    __totalAnimales=0
    def __init__(self, nombre, edad, habitat, genero):
        self.__nombre=nombre
        self.__edad=edad
        self.__habitat=habitat
        self.__genero=genero
        self.__zona=[]
        
#metodos get

    def getNombre(self):
        return self.__nombre
    
    @classmethod
    def getTotalAnimales(cls):
        return cls.__totalAnimales

    def getEdad(self):
        return self.__edad

    def getHabitat(self):
        return self.__habitat

    def getGenero(self):
        return self.__genero

    def getZona(self):
        return self.__zona

#metodos sett

    def setNombre(self,nombre):
        self.__nombre=nombre

    def setEdad(self,edad):
        self.__edad=edad

    def setHabitat(self, habitat):
        self.__habitat=habitat

    def setGenero(self, genero):
        self.__genero=genero

    def setZona(self, zona):
        self.__zona=zona

#metodos de la clase 

    def movimiento(self):
        return "desplazarse"


    def toString(self):
        if self.__zona:
            imprimir= "Mi nombre es "+self.__nombre+", tengo una edad de "+str(self.__edad)+", habito en "+self.__habitat+" y mi genero es "+self.__genero+", la zona en la que me ubico es: "+self.__zona.getNombre()
            
        else: 
            imprimir="Mi nombre es "+self.__nombre+", tengo una edad de "+str(self.__edad)+", habito en "+self.__habitat+" y mi genero es "+self.__genero
        return imprimir 

    @classmethod
    def totalPorTipo(cls):
        return f"Mamiferos : {Mamifero.cantidadMamiferos()}\nAves : {Ave.cantidadAves()}\nReptiles : {Reptil.cantidadReptiles()}\nPeces : {Pez.cantidadPeces()}\nAnfibios : {Anfibio.cantidadAnfibios()}"
     

