from veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, codigo, marca, modelo, ano, valor_diaria,quantidade_portas):
        super().__init__(codigo, marca, modelo, ano, valor_diaria)
        self.quantidade_portas = quantidade_portas

    def exibir_carro(self):
        print("\n --- Carro ---")
        self.exibir_dados()
        print(f"quantidade de portas: {self.quantidade_portas}")