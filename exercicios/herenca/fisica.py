from pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, end, fone, cpf):
        Pessoa.__init__(self, codigo, nome, end, fone)
        self.cpf = cpf