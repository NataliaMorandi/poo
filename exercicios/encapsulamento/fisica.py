from pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def imprimirCPF(self):
        print("CPF: ", self.__cpf)

    def calculaIMC(self):
        imc =  self.altura/self.peso 
        return imc
    