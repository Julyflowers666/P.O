from produto import Produto

class Bebida(Produto):
    def __init__(self, nome, preco, codigo, ml):
        super().__init__(nome, preco, codigo)
        self.ml = ml

    def calcular_preco(self):

        preco = self.get_preco()

        if self.ml > 500:
            preco += 3
        return preco