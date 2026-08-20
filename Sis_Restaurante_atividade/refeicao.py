from produto import Produto

class Refeicao(Produto):
    def __init__(self,pegueno,grande,familia):
        self.pegueno = pegueno
        self.grande = grande
        self.familia = familia

    