from cliente import Cliente
from produto import Produto

class Pedidos:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []
        self.status = "aberto"


    def adicionar_produto(self, produto):

        if self.status == "fechado":
            print("Pedido fechado.")
            print("Não é possível adicionar produtos.")
            return False
        else:
            self.produtos.append(produto)

            print(f"{produto.get_nome()} " f"adicionado ao pedido.")
            return True

    def calcular_total(self):
        total = 0

        for produto in self.produtos:
            total += produto.calcular_preco()
        return total

    def fechar_pedido(self):

        if len(self.produtos) == 0:
            print("Não é possível finalizar o pedido.")
            print("Adicione pelo menos um produto.")
            return False
        else:

            self.status = "fechado"
            print("Pedido fechado!")
            return True
    
    def exibir_pedido(self):

        print("\n========== PEDIDO ==========")
        print(f"Cliente: {self.cliente.get_nome()}")
        print(f"Código: {self.codigo}")
        print("\nProdutos:")

        if len(self.produtos) == 0:
            print("Nenhum produto.")
        else:
            for produto in self.produtos:
                print(f"- {produto.get_nome()}" f"R$ {produto.calcular_preco():.2f}")

        print("----------------------------")
        print(f"TOTAL:R$ " f"{self.calcular_total():.2f}")
        print(f"STATUS: {self.status}")