from aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, cod, nome, matricula, semestre):
        Aluno.__init__(self, cod, nome, matricula)
        self.semestre = semestre
    
    def imprimir(self):
        super().imprimir()
        print("semestre", self.semestre)
