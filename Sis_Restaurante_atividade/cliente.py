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

        while True:
            
            telefone = input("Digite o seu telefone (com DDD): ")
# Remove espaços ou caracteres especiais, se quiser
            telefone_limpo = "".join(filter(str.isdigit, telefone))
# Verifica se o tamanho tem 10 ou 11 dígitos (ex: 11988887777)
            if len(telefone_limpo) == 11 or len(telefone_limpo) == 10:
                print("Telefone válido!")
            else:
                print("Telefone inválido. Digite o número com DDD.")

    def exibir_dados(self):

        print("----------dados do cliente----------")
        print(f"Código: {self.codigo}")
        print(f"Nome: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
