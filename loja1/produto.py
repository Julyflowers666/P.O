class Produto:
    def __init__(self,codigo,descricao,preco,quantidade):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def Mostrar_dados(self):
        print("----Dados----")
        print(f"codigo do Produto: {self.codigo}")
        print(f"descrição: {self.descricao}")
        print(f"preço: {self.preco}")
        print(f"quantidade: {self.quantidade}")

    def calcular (self):
        total = self.preco * self.quantidade
        print(f"total do estoque: {total}")

    def adicionar(self,quantidade):
        total = self.quantidade + quantidade
        self.quantidade = total
        print(f"quantidade adicionada: {total}")

    def retirar(self,quantidade):
        total = self.quantidade - quantidade
        self.quantidade = total
        print(f"quantidade retirada: {total}")