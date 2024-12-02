from Carros import Carros

class Fila():
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def registrar(self, modelo, placa):
        carro = Carros(modelo, placa)
        if self.inicio == None:
            self.inicio = carro

        else:
            self.fim.proximo = carro
        self.fim = carro
        self.tamanho += 1

    def imprimir(self):
        if self.inicio == None:
            print('sem carros')

        else:
            print("Fila com ", self.tamanho, " carros")
            
            ponteiro = self.inicio
            texto = ""
            while ponteiro:
                texto += f"{ponteiro.modelo} + {ponteiro.placa}\n"
                ponteiro = ponteiro.proximo
            print(texto)          


    def retirar(self):
        if self.inicio == self.fim:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
        self.tamanho -= 1
        self.imprimir()