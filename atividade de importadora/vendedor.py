class Vendedor:

    def __init__(self, id, nome, idade, cpf):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def vender (self):
        print(f"vendedor:",self.nome + " vendeu!")

    def __str__(self):
        return ("vendedor: ", self.nome, "idade: ", self.idade,"id: ", self.id, "cpf: ", self.cpf)
