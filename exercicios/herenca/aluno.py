class Aluno:
    def __init__(self, cod, nome, matricula):
        self.cod = cod
        self.nome = nome
        self.matricula = matricula

    def imprimir(self):
        print("codigo: ", self.cod)
        print("nome: ", self.nome)
        print("matricula: ", self.matricula)


