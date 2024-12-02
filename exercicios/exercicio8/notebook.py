from computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        super().getInformacoes()
        print(f"Tempo de Bateria: {self.__tempoDeBateria} horas.")

    def cadastrar(self):
        pass


