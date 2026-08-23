from produto import Produto

class Funcionario:
    def __init__(self,nome,telefone,codigo):
        self.__nome = nome
        self.__telefone = telefone
        self.codigo = codigo
        self.__funcionarios = []

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
# Verifica se o tamanho tem 10 ou 11 dígitos (ex: 11988887777), meu tratamento de erro q tava dando erro que ele tinha que tratar,desist
            if len(telefone_limpo) == 11 or len(telefone_limpo) == 10:
                print("Telefone válido!")
            else:
                print("Telefone inválido. Digite o número com DDD.")

    def get_funcionarios(self):
        return self.__funcionarios
    
    def cadastrar_produto(self):
        if len(self.__funcionarios) == 0:
            print("nenhum funcionário cadastrado.")
            print("Cadastre um funcionário antes de cadastrar produtos.")
            return

        print("------CADASTRAR PRODUTO ----")

        while True:
            nome = input("Digite o nome do produto: ").strip()

            if nome == "":
                print("O nome não pode ficar vazio.")

            elif nome.isdigit():

                print("O nome não pode ser números.")
            else:
                break

        while True:
            try:
                preco = float(input("Digite o preço do produto: R$ "))
                if preco <= 0:
                    print("O preço deve ser maior que zero.")
                else:
                    break

            except ValueError:
                print("digite apenas numeros")

        while True:
            try:
                codigo = int(input("Digite o codigo do produto: "))
                if codigo <= 0:
                    print("O codigo deve ser maior que zero.")
                else:
                    break

            except ValueError:
                print("digite apenas numeros")

        produto = Produto(nome, preco, codigo)
        print("Produto cadastrado com sucesso!")
        return produto

    def exibir_dados_Funcionario(self):
        print("-------dados do funcioario------")
        print(f"Nome: {self.__nome}")
        print(f"telefone: {self.__telefone}")
        print(f"Código: {self.codigo}")

#Funcionario.cadastrar_produto()