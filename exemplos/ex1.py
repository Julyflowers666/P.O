class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.nome = preco
        self.quantidade = quantidade

    def mostrar_dados(self):
        print("produto: ", self.nome)
        print("preço: ", self.preco)
        print("quantidade em estoque: ", self.quantidade)

    def calcular_total(self):
        total = self.preco * self.quantidade
        print(f"valor total em estoque: R$ {total:.2f}")

p1 = Produto ("mouse",50.00, 10)
p2 = Produto ("teclado", 120.00, 5)

p1.mostrar_dados()
p1.calcular_total()

p2.mostrar_dados()
p2.calcular_total()