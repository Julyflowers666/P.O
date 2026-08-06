from veiculos import Veiculos

class Moto(Veiculos):
    def __init__(self, codigo, marca, modelo, ano, valor_diaria, cilindrada):
        super().__init__(codigo, marca, modelo, ano, valor_diaria)
        self.cilindrada = cilindrada

    def exibir_moto (self):
        print("\n--- Moto --- ")
        self.exibir_dados()
        print(f"cilindrada: {self.cilindrada}")