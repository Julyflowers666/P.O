class Produto:
    def __init__(self,nome,preco,codigo):
        self.__nome = nome
        self.__preco = preco
        self.codigo = codigo

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco <= 0:
            print("O preço deve ser maior que zero.")
            return False

        self.__preco = preco
        return True

    def calcular_preco(self):
        return self.__preco
    #preço original ante de passar pela regra, polimorfismo
    

    def exibir_produto(self):
        print (f"Código: {self.codigo}" f" {self.__nome} - "f"R$ {self.calcular_preco():.2f}")

