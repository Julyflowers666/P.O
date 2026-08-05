class Paciente:
    def __init__(self,codigo,nome,cpf,idade):
        self.codigo = codigo
        self.__nome = nome
        self.__cpf = cpf
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome.strip() == "":
            print("nome é invalido")
        else:
            self.__nome = nome
            print("Nome atualizada")

#leitura do dado
    def get_cpf(self):
        return self.__cpf

#alteração, coloca regras
    def set_cpf(self, cpf):
        cpf = cpf.replace (".","").replace("-","")

        if len(cpf) == 11 and cpf.isdigit():
            self.__cpf = cpf
            print("cpf atualizado")
        else:
            print("cpf invalido")

    def get_idade(self):
        return self.__idade

    def set_idade(self,idade):
        if idade >=0:
            self.__idade = idade
        else:
            print("idade invalida")

    def exibir_dados(self):
        print(f'\n----Paciente---')
        print(f"codigo: {self.codigo}")
        print(f"Nome: {self.get_nome()}")
        print(f"Cpf: {self.get_cpf()}")
        print(f"idade: {self.get_idade()}")
                