from veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaMotor):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.potenciaMotor = potenciaMotor

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print("potenciaMotor: ", self.potenciaMotor)

