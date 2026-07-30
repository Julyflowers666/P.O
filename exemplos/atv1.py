class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def dados (self):
        print("marca do carro: ", self.marca)
        print("modelo do carro: ", self.modelo)
        print("ano do carro: ", self.ano)
        print("velocidade: ", self.velocidade)

    def acelerar (self):
        self.velocidade = self.velocidade + 10
        print (f"a velocidade do carro é: {self.velocidade}")

    def frear (self):
        self.velocidade = self.velocidade - 10
        if self.velocidade >= 0:
            print (f"a velocidade do carro é: {self.velocidade}")
        elif self.velocidade <0:
            print ("a velocidade do carro é negativo!")

carro = Carro ("Volkswagen","fusca", 1986, 0)

carro.dados()
carro.acelerar()
carro.frear()
carro.frear()