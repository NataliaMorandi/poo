from computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        super().getInformacoes()
        print("Potencia da Fonte: ", self._potenciaDaFonte)

        #ou
        #return super().getInformacoes() + ", " + self._potencialDaFonte

    def cadastrar(self):
        self.modelo = input("digite o modelo: ")
        self.cor = input("Digite a cor: ")
        self.preco = input("Digite o preço: ")

