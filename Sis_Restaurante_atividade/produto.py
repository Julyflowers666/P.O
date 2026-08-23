class Produto:
    def __init__(self,nome,preco,codigo):
        self.nome = nome
        self.__preco = preco
        self.codigo = codigo

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco <= 0:
            print("O preço deve ser maior que zero.")

    def get_nome(self):
        return self.__nome

    def exibir_produto(self):
        print(f"{self.__nome} - R$ {self.__preco:.2f}")

