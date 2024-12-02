from aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, cod, nome, matricula, ano):
        Aluno.__init__(self, cod, nome, matricula)
        self.ano = ano

    def imprimir(self):
        #super().imprimir()
        Aluno.imprimir(self)
        print("ano: ", self.ano)

