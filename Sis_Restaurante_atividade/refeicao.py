from produto import Produto

class Refeicao(Produto):
    def __init__(self, nome, preco, codigo, tamanho):
        super().__init__(nome, preco, codigo)
        self.tamanho = tamanho

    def calcular_preco(self):

        preco = self.get_preco()

        if self.tamanho.lower() == "grande":
            preco = preco * 1.20
        return preco

    