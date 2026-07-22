class Produtos:
    def __init__(self, id, nome, preco, estoque, tipo):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.tipo = tipo

    def __str__(self):
        return ("Produto: " + self.nome + " preço: " + str(self.preco) + " estoque: " + str(self.estoque) + " Tipo: " + self.tipo)

