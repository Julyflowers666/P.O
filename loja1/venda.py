class Venda:
    def __init__(self,cliente,produto,quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade

    def finaliza_venda(self):
        if self.quantidade <=0:
            print("quantidade é invalidada")
            return
        
        if self.quantidade > self.produto.quantidade:
            print("venda não realizada.estoque insuficiente")

        total = self.produto.preco * self.quantidade
        self.produto.retirar(self.quantidade)

        print("\n---Vendas finalizada---")
        print(f"cliente: {self.cliente.nome}")
        print(f"produto: {self.produto.descricao}")
        print(f"quantidade: {self.quantidade}")
        print(f"total: R$ {total:2f}")
