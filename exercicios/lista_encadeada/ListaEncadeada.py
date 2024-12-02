from No import No

class ListaEncadeada:

    def __init__(self):
        self.inicio = None #aponta para nó 'aa' endereço 2

    def addInicio(self, valor):
        nodo = No( valor) #cria nó
        if self.inicio is not None: #confere se já tem algo na lista
            nodo.prox = self.inicio #aponta nodo.prox para o atual self.inicio que é 'aa'
        self.inicio = nodo #self.inicio vira 'ff'
        self.imprimir()

    def addFim(self, valor): #cria nó > se lista for vazia só adiciona o novo nó
                             #se lista não estiver vazia, 
        nodo = No( valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio 
            while aux.prox: 
                aux = aux.prox 
            aux.prox = nodo 
        self.imprimir()
    
    def imprimir(self):
        print("------------------------")
        if self.inicio == None:
            print("Lista Encadeada está vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox
        print("------------------------")

    def removerInicio(self):
        if self.inicio == None:
            print("Nenhum elemento removido")
        else:
            self.inicio = self.inicio.prox
        self.imprimir()

    def removerFim(self):
        if self.inicio == None:
            print("Nenhum elemento removido")
        else:
            if self.inicio.prox == None:
                self.inicio = None
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux.prox:
                    ant = aux
                    aux = aux.prox
                ant.prox = None
        self.imprimir()

    def addOrdenado(self, valor):
        nodo = No(valor)
        if self.inicio is None or self.inicio.dado >= valor:  # Caso 1: Lista vazia ou inserir no início.
            nodo.prox = self.inicio
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.prox and aux.prox.dado < valor:  # Encontrar a posição correta.
                aux = aux.prox
            nodo.prox = aux.prox  # Ajusta o próximo do novo nó.
            aux.prox = nodo  # Insere o novo nó na posição correta.
        self.imprimir()