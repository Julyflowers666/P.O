from bebida import Bebida
from cliente import Cliente
from funcionario import Funcionario, lista_funcionarios
from pedido import Pedidos
from produto import Produto
from refeicao import Refeicao
from sobremesa import Sobremesa

def cadastrar_funcionario():
    print("\n--- CADASTRO DO FUNCIONARIO ---")
    while True:
        try:
            codigo = int(input("Informe o seu código: "))
            break
        except ValueError:
            print("Digite um código numérico válido.")
    while True:
        
        telefone = input("Digite o seu telefone (com DDD): ")
    
        telefone_limpo = "".join(filter(str.isdigit, telefone))
    
        if len(telefone_limpo) == 11 or len(telefone_limpo) == 10:
            print("Telefone válido!")
        else:
            print("Telefone inválido. Digite o número com DDD.")
            return cadastrar_funcionario()
        
        while True:
            nome = input("Informe seu nome: ").strip()
            
            if len(nome) >= 3:
                break
            print("O nome deve possuir pelo menos três caracteres.")

        funcionario = Funcionario (nome, telefone,codigo)
        lista_funcionarios.append(funcionario)
        print("Funcionário cadastrado com sucesso!")

        for funcionario in lista_funcionarios:
            funcionario.exibir_dados_Funcionario()

        #return funcionario
        #funcionarios.append(funcionario)
        #return funcionarios


def cadastrar_cliente():
    print("\n--- CADASTRO DO CLIENTE ---")
    while True:
        try:
            codigo = int(input("Informe o seu código: "))
            break
        except ValueError:
            print("Digite um código numérico válido.")

    while True:
        nome = input("Informe seu nome: ").strip()

        if len(nome) >= 3:
            break

        print("O nome deve possuir pelo menos três caracteres.")

    while True:
            
            telefone = input("Digite o seu telefone (com DDD): ")

            telefone_limpo = "".join(filter(str.isdigit, telefone))

            if len(telefone_limpo) == 11 or len(telefone_limpo) == 10:
                print("Telefone válido!")
            else:
                print("Telefone inválido. Digite o número com DDD.")
                return cadastrar_cliente()

            return Cliente(codigo, nome, telefone)
            

def Menu():

    print("------------------------------")
    print("   SISTEMA DE PEDIDOS DE RESTAURANTE      ")
    print("------------------------------")
    while True:
        print("--------- MENU ----------")
        print("1- Cadastrar Cliente")
        print("2- Cadastrar Funcionario")
        print("3- Cadastrar produto")
        print("4- Listar produtos")
        print("0- Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            cadastrar_cliente()
        elif op == "2":
            cadastrar_funcionario()
        elif op == "3":
            Funcionario.cadastrar_produto()
            Produto.exibir_produto()

        elif op == "4":
            Produto.exibir_produto()

        elif op == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    Menu()

funcionario1 = Funcionario("João", "12345678911", "00123")
produto1 = Produto("laranja",12.00,"00056")