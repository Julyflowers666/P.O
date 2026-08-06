class Cliente:
    def __init__(self,codigo,nome,cpf):
        self.codigo = codigo #publico
        self.__nome = nome #privado
        self.__cpf = cpf #privado

    #Setter para validar dados recebidos
        self.set_nome(nome)
        self.set_cpf(cpf)

    def get_nome(self):
        #Retorna o nome do cliente
        return self.__nome

    def set_nome(self, nome):
        #altera o nome do cliente
        nome = nome.strip()

        if len(nome) < 3:
            print("error: o nome deve possuir pelo menos três caracteres")

        self.__nome = nome
        return True

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        cpf = cpf.replace (".","").replace("-","")
    
        if len(cpf) == 11 and cpf.isdigit():
            self.__cpf = cpf
            print("cpf atualizado")
        else:
            print("cpf invalido")

        self.__cpf = cpf
        return True

    def exibir_dados(self):
        print("---Dados do Cliente---")
        print(f"codigo: {self.codigo}")
        print(f"nome: {self.__nome}")
        print(f"cpf: {self.__cpf}")


    
