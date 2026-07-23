class Pagamentos:
    def __init__(self, pix, cartao, vale):
        self.pix = pix
        self.cartao = cartao
        self.vale = vale

    def __str__(self):
        return (f"metados de pagamentos: {self.pix} + {self.cartao} + {self.vale}") 