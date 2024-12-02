from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, partidaEletrica):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.partidaEletrica = partidaEletrica

    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print("Partida Eletrica: ", self.partidaEletrica)