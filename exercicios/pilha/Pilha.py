from Livro import Livro

class Pilha():
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def inserir(self, livro):
        if self.topo != None: 
            livro.proximo = self.topo
        self.topo = livro
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("\nTotal ", self.tamanho)
        ponteiro = self.topo
        while ponteiro:
            print(ponteiro)
            ponteiro = ponteiro.proximo

    def remover(self):
        if self.topo == None:
            print("Lista vazia")
        else:
            self.topo = self.topo.proximo
            self.tamanho -= 1
            self.imprimir()


    