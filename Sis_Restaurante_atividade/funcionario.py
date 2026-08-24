from produto import Produto
from refeicao import Refeicao
from bebida import Bebida
from sobremesa import Sobremesa

lista_funcionarios = []

class Funcionario:
    def __init__(self,nome,telefone,codigo):
        self.__nome = ""
        self.__telefone = ""
        self.codigo = codigo
        #self.__funcionarios = []

        self.set_nome(nome)
        self.set_telefone(telefone)

    def get_nome(self):
                
            return self.__nome
        
    def set_nome(self, nome):

        nome = nome.strip()

        if len(nome) < 3:
            print("Erro: o nome deve possuir pelo menos três caracteres.")
            return False
        elif not nome.replace(" ", "").isalpha():
            print("Não é permitido números ou símbolos.")

        self.__nome = nome
        return True

    def get_telefone(self):
        return self.__telefone

    def set_telefone(self,telefone):

        while True:  
            telefone_limpo = "".join(filter(str.isdigit, telefone))

            if len(telefone_limpo) == 11 or len(telefone_limpo) == 10:
                self.__telefone = telefone_limpo
                return True
            else:
                print("Telefone inválido. Digite o número com DDD.")
                return False

    @staticmethod
#faz com que não precise de um funcionario em expecifico para fazer um cadastro de produto :p
    def cadastrar_produto():
        if len(lista_funcionarios) == 0:
            print("nenhum funcionário cadastrado.")
            print("Cadastre um funcionário antes de cadastrar produtos.")
            return

        print("------CADASTRAR PRODUTO ----")

        while True:
            print("1- Refeição")
            print("2- Bebida")
            print("3- sobremesa")
            try:
                op = int(input("Escolha qual tipo de produto ira cadastrar: "))
            except ValueError:
                print("digite apenas numero")
                continue

            if op == 1:
                while True:
                    print("escolha: Refeição")
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

                while True:

                    tamanho = input("Digite o tamanho (pequeno/medio/grande): ").strip().lower()

                    if tamanho in ["pequeno", "medio", "grande"]:
                        break

                    print("Digite pequeno, medio ou grande.")

                produto = Refeicao(nome, preco, codigo, tamanho)
                break

            elif op == 2:
                while True:
                    print("escolha: Bebida")
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
                while True:
                    try:
                        ml = int(input("Digite a quantidade em ml: "))
                    
                        if ml <= 0:
                            print("A quantidade deve ser maior que zero.")

                        else:
                            break

                    except ValueError:
                        print("digite apenas numeros (em ml)")

                produto = Bebida(nome, preco, codigo, ml)

            elif op == 3:
                while True:
                    print("escolha: sobremesa")
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

                while True:
                        especial = input("A sobremesa é especial? (sim/nao): ").strip().lower()

                        if especial == "sim" or especial == "nao":
                            break

                        print("Digite apenas sim ou nao.")

                produto = Sobremesa(nome, preco, codigo, especial)

            else:
                print("Opção inválida.")
                return None

            print("Produto cadastrado com sucesso!")
            return produto

    def exibir_dados_Funcionario(self):
        print("-------dados do funcioario------")
        print(f"Nome: {self.__nome}")
        print(f"telefone: {self.__telefone}")
        print(f"Código: {self.codigo}")

#Funcionario.cadastrar_produto()