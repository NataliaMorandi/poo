from pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricaoEstadual, qtdFuncionarios):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual
        self.qtdFuncionarios = qtdFuncionarios

    def imprimirCNPJ(self):
        print ("CNPJ: ", self.__cnpj)

    def emitirNotaFiscal(self):
        pass
    