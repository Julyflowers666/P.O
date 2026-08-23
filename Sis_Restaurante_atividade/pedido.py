from cliente import Cliente
from produto import Produto

class Pedidos (Produto):
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []
        self.status = "aberto"
        

    def Fazer_pedido(self, Produto):

        self.produtos.append(produto)

        print(f"{produto.get_nome()} foi adicionado ao pedido.")

        return True

        if self.status == "fechado":
            print("O pedido já está fechado!")
            print("Não é possível adicionar novos produtos.")
            return False

    def exibir_dados(self):

        print(f"Código: {self.codigo}")
        print(f"Pedido: {self.nome}")
        print(f"Status: {self.status}")