from funcionario import Funcionario

funcionario1 = Funcionario ("13523", "july","design","1000")

funcionario1.exibir_dados()

print("\n tentando alterar o salario para negativo")
funcionario1.set_salario(-500)
funcionario1.set_salario(11000)