from bebida import Bebida
from cliente import Cliente
from funcionario import Funcionario, lista_funcionarios
from pedido import Pedidos
from produto import Produto
from refeicao import Refeicao
from sobremesa import Sobremesa

clientes = []
lista_produtos = produtos()

def menu():
    while True:
        print("-----Menu Refeições------")


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
                break
            else:
                print("Telefone inválido. Digite o número com DDD.")
        
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
                break
            else:
                print("Telefone inválido. Digite o número com DDD.")

    return Cliente(codigo, nome, telefone)           

def Sistema_principal():

    print("------------------------------")
    print("   SISTEMA DE PEDIDOS DE RESTAURANTE      ")
    print("------------------------------")
    while True:

        print("--------- MENU ----------")
        print("1- Fazer Pedido")
        print("2- Cadastrar Cliente")
        print("3- Cadastrar Funcionario")
        print("4- Cadastrar produto")
        print("5- Listar produtos")
        print("6- Ver Dados dos Clientes")
        print("7- Ver Dados do Funcionarios")
        print("0- Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            Pedidos

        elif op == "2":
            cliente = cadastrar_cliente()
            clientes.append(cliente)
            print("Cliente cadastrado com sucesso!")
        elif op == "3":
            cadastrar_funcionario()
        elif op == "4":
            produto = Funcionario.cadastrar_produto()
            if produto is not None:
                lista_produtos.append(produto)

            if len(lista_produtos) == 0:
                print("Nenhum produto cadastrado.")
            else:
                print("\n========== PRODUTOS ==========")
            for produto in lista_produtos:
                produto.exibir_produto()
                print("----------------------------")

        elif op == "5":
            Produto.exibir_produto()
        elif op == "6":
            for cliente in clientes:
                cliente.exibir_dados()
        elif op == "7":
            for funcionario in lista_funcionarios:
                funcionario.exibir_dados_Funcionario()
        elif op == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")

def produtos ():
    lista_de_produtos =[]
    produto1 = Produto("Hambúrguer", 25.00, 12, "grande")
    produto2 = Produto("Batata Frita", 12.00, 13)

    produto3 = Produto("Refrigerante", 7.00, 7, 400)
    produto4 = Produto("Refrigerante", 7, 9, 600)

    produto5 = Produto("Hambúrguer", 25.00, 11, "Medio")
    
    produto6 = Sobremesa("Pudim",20.00, 20, "especial")

    return [produto1, produto2, produto3, produto4, produto5, produto6]

#def funcionarios ():
#
#   funcionario1 = Funcionario("João", "12345678911", 123)
#    funcionario2 = Funcionario("ana", "12345678912", 132)
#    funcionario3 = Funcionario("vitor", "12345678913", 143)

#    return [funcionario1,funcionario2, funcionario3]

#def cliente():
#    cliente1 = Cliente(144, "clara", "1234567899")
#
#    return [cliente1]



if __name__ == "__main__":
    Sistema_principal()