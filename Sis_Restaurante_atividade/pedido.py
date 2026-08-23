from cliente import Cliente
from produto import Produto

class Pedidos(Cliente, Produto):
    def __init__(self, codigo, nome, status, telefone):
        super().__init__(codigo, nome,telefone, status,)
        self.status = "indisponivel"
        self.codigo = codigo
        


    def exibir_dados(self):

        print(f"Código: {self.codigo}")
        print(f"Pedido: {self.nome}")
        print(f"Status: {self.status}")