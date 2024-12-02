from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, valor):

        # alocar na memoria (instanciar o nó)
        # inserir apos o ultimo
        # atualizar fim

        nodo = No(valor) 
        if self.inicio == None:
            self.inicio = nodo

        else:
            self.fim.proximo = nodo # Atualiza o próximo do último nó para o novo nó.
        self.fim = nodo # Atualiza 'fim' para apontar para o novo nó.
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print("Fila vazia")
        else:
            print("Fila com ", self.tamanho, " elementos")
            ponteiro = self.inicio
            texto = ""
            while ponteiro:
                texto += ponteiro.dado + " - "
                ponteiro = ponteiro.proximo
                print(texto)

    def remover(self):
        
        # atribui a variavel auxiliar o proximo do primeiro elemento da fila
        # remove o primeiro
        # atribui a inicio o valor da variavel auxiliar
        # se a fila ficar vazia, atribui null para inicio e fim
        if self.inicio.proximo == None:
            self.fim = None
        ...
        ...
        self.inicio = self.inicio.proximo
        self.tamanho -= 1
        self.imprimir()
        ...
        ...
