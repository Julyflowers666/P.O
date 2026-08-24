from produto import Produto

class Sobremesa(Produto):
        def __init__(self, nome, preco, codigo, especial):
            super().__init__(nome, preco, codigo)
            self.especial = especial

        def calcular_preco(self):

            preco = self.get_preco()

            if self.especial.lower() == "sim":
                preco = preco * 1.15
            return preco