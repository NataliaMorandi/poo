from Livro import Livro
from Pilha import Pilha

l1 = Livro("O tempo e o Vento", "Érico Veríssimo", 220)
l2 = Livro("Dom Casmurro", "Machado de Assis", 524)
l3 = Livro("Senhor dos Anéis", "Tolkien", 875)
l4 = Livro("Guerra dos Tronos", "George Martins", 654)

pilha = Pilha()
pilha.imprimir()

pilha.inserir(l1)
pilha.inserir(l2)
pilha.inserir(l3)
pilha.remover()
pilha.inserir(l4)
pilha.remover()
pilha.remover()
pilha.remover()
pilha.remover()