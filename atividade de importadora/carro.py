class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar():
        print("carro acelerar")

    def freiar():
        print("carro freiando")

    def __str__(self):
        return ("Carro: " + self.marca + " modelo: " + self.modelo + " ano: " + str(self.ano) + " velocidade: " + str(self.velocidade))
    