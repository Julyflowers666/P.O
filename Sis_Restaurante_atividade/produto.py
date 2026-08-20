class Produto:
    def __init__(self,codigo,nome,preço):
        self.codigo = codigo
        self.nome = nome
        self.__preço = preço