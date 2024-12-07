from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marcas, modelo, ano, nPortas):
        super().__init__(marcas, modelo, ano)
        self.__nPortas=nPortas
    
    # Métodos set
    def setNPortas(self, portas):
        self.__nPortas=portas
    # Métodos get
    def getNPortas(self):
        return self.__nPortas
    def mostrar(self):
        return(f"Carro da marca: {self.getMarca()}, Modelo: {self.getModelo()}, Ano: {self.getAno()}, e Portas: {self.getNPortas()}")
    
#c=Carro("VW", "Gol", 2000, 5)
#print(c.mostrar())