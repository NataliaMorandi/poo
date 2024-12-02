class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirInformacoes(self):
        print(f"Marca: {self.marca}\nQuant. rodas: {self.qtdRodas}\nModelo: {self.modelo}\nVelocidade: {self.velocidade}")

    def acelerar(self, velocidadeAtual):
        if self.velocidade < velocidadeAtual:
            return self.velocidade + velocidadeAtual

    def frear(self, velocidadeAtual):
        if self.velocidade > velocidadeAtual:
            return self.velocidade - velocidadeAtual

