class Cliente:
    def __init__(self,codigo, nome, cpf):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf

    def exibir_dados(self):
        print("----Dados----")
        print(f"codigo: {self.codigo}")
        print(f"nome: {self.nome}")
        print(f"cpf: {self.cpf}")