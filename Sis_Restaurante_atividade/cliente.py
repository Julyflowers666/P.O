class Cliente:
    def __init__(self,codigo,nome,telefone):
        self.codigo = codigo
        self.__nome = nome
        self.__telefone = telefone

    def get_nome(self):
                
            return self.__nome
        
    def set_nome(self, nome):

        nome = nome.strip()

        if len(nome) < 3:
            print("Erro: o nome deve possuir pelo menos três caracteres.")
            return False

        self.__nome = nome
        return True

    def get_telefone(self):
         return self.__telefone

    def set_telefone(self,telefone):

        if telefone <= 0:
            print("Error: o telefone tem q possuir 9 numeros ")
        
    

    def exibir_dados(self):

        print(f"Código: {self.codigo}")
        print(f"Nome: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
