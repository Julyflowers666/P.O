class Funcionario:
    def __init__(self,matricula,nome,cargo,salario):
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibir_dados(self):
        print(f"matricula: {self.matricula}")
        print(f"nome: {self.nome}")
        print(f"cargo: {self.cargo}")
        print(f"salario: {self.salario}")

    def alterar_cargo(self, novo_cargo):
        self.cargo = novo_cargo
        print(f"o cargo foi alterado: {self.cargo}")

    def aplicar_reajuste(self,percentual):
        aumento = self.salario * percentual / 100
        self.salario += aumento


funcionario1 = Funcionario (1245,"carlos","faxineiro",1000)
funcionario1.exibir_dados()
funcionario1.alterar_cargo ("estagiario")
funcionario1.aplicar_reajuste(10)
funcionario1.exibir_dados()


