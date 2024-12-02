from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, qtdPortas):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.qtdPortas = qtdPortas

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("Quantidade de portas: ", self.qtdPortas)