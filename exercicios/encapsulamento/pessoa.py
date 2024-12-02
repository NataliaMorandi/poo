class Pessoa:
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimirNome(self):
        print("Nome: ", self.nome)

    #def __str__(self):
    #    txt = "Nome: " + self.nome
    #    return txt

    def getimprimirTelefone(self):
        return self.__telefone

    