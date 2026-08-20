from cliente import Cliente
from produto import Produto

class Pedidos(Cliente, Produto):
    def __init__(self,codigo,nome,preço):
        self.codigo = codigo
        self.nome = nome
        self.preço = preço

    def exibir_dados(self):

        print(f"Código: {self.codigo}")
        print(f"Marca: {self.nome}")
        print(f"Modelo: {self.modelo}")