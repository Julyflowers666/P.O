from paciente import Paciente

paciente1 = Paciente(1,"July",12345678900,20)

#print(f"\n alterando nome para vazio")
#paciente1.set_nome("")

print(f"\n alterando nome")
paciente1.set_nome("jullyana")

print(f"\n alterando cpf")
paciente1.set_cpf("123-456-789-10")

print(f"\n alterando idade")
paciente1.set_idade(24)

paciente1.exibir_dados()