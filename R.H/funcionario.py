class Funcionario:
    def __init__(self, matricula, nome, cargo, salario):
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        if novo_salario < 1600:
            print("error, salario abaixo do permitido")
        elif novo_salario > 10000:
            print("error, salario muito alto")
        else:
            self.__salario = novo_salario
            print("salario Atulizado")

    def exibir_dados(self):
        print("---funcionario---")
        print(f"matricula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"salario: {self.__salario}")