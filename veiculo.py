from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, marcas, modelo, ano):
        self.__marca=marcas
        self.__modulo=modelo
        self.__ano=ano
    
    # Métodos get
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modulo
    def getAno(self):
        return self.__ano
    
    # Métodos set
    def setMarca(self, marca):
        self.__marca=marca
    def setModelo(self, modelo):
        self.__modelo=modelo
    def setAno(self, ano):
        self.__ano=ano
    
    @abstractmethod
    def mostrar(self):
        pass