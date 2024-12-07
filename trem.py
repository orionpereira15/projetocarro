from veiculo import Veiculo

class Trem(Veiculo):
    def __init__(self, marcas, modelo, ano, nVagoes):
        super().__init__(marcas, modelo, ano)
        self.__nVagoes=nVagoes
    
    def setNVagoes(self, vagoes):
        self.__nVagoes=vagoes
    def getNVagoes(self):
        return self.__nVagoes
    def mostrar(self):
        return(f"Trem da marca: {self.getMarca()}, Modelo: {self.getModelo()}, Ano: {self.getAno()}, e Vagoes: {self.getNVagoes()}")
    
#t = Trem("v", "N", 1200, 5)
#print(t.mostrar())