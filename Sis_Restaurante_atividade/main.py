from bebida import Bebida
from cliente import Cliente
from funcionario import Funcionario, lista_funcionarios
from pedido import Pedidos
from produto import Produto
from refeicao import Refeicao
from sobremesa import Sobremesa

def selecionar_cliente():

    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
        return None

    print("\n========== CLIENTES ==========")

    for cliente in clientes:
        print(f"Código: {cliente.get_codigo()} | Nome: {cliente.get_nome()}")

    try:
        codigo = int(input("Digite o código do cliente: "))
    except ValueError:
        print("Digite apenas números.")
        return None

    for cliente in clientes:
        if cliente.get_codigo() == codigo:
            return cliente

    print("Cliente não encontrado.")
    return None

def Fazer_pedido(cliente, lista_produtos):

    pedido = Pedidos(cliente) 

    while True:
        print("========== MENU DO PEDIDO ==========")
        print("1 - Adicionar produto")
        print("2 - Exibir pedido")
        print("3 - Finalizar pedido")
        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números.")
            continue

        if op == 1:

            if len(lista_produtos) == 0:
                print("Nenhum produto cadastrado.")
                continue

            print("\n========== PRODUTOS ==========")

            for produto in lista_produtos:
                print(f"Código: {produto.codigo} | "f"Nome: {produto.get_nome()} | "f"Preço: R$ {produto.calcular_preco():.2f}")

            
            try:
                codigo = int(input("\nDigite o código do produto: "))

            except ValueError:
                print("Digite apenas números.")
                continue

            produto_encontrado = None

            for produto in lista_produtos:

                if produto.codigo == codigo:
                    produto_encontrado = produto
                    break

            if produto_encontrado is None:
                print("Produto não encontrado.")
                continue

            pedido.adicionar_produto(produto_encontrado)

        elif op == 2:
            pedido.exibir_pedido()

        elif op == 3:
            if pedido.fechar_pedido():
                pedido.exibir_pedido()
                break

        else:
            print("Opção inválida.")


def cadastrar_funcionario():
    print("\n--- CADASTRO DO FUNCIONARIO ---")
    while True:
        try:
            nome = input("Informe seu nome: ").strip()
                
            if len(nome) < 3:
                print("O nome deve possuir pelo menos três caracteres.")

            elif not nome.replace(" ", "").isalpha():
                print("Não é permitido números ou símbolos.")
            else:
                break
                
        except ValueError:
            print("não é permitido numeros") 

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
        
    funcionario = Funcionario (nome, telefone,codigo)
    lista_funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")

    for funcionario in lista_funcionarios:
        funcionario.exibir_dados_Funcionario()

    #return funcionario
    #funcionarios.append(funcionario)
    #return funcionarios
    #errado


def cadastrar_cliente():
    print("\n--- CADASTRO DO CLIENTE ---")
    while True:
        try:
            codigo = int(input("Informe o seu código: "))
            break
        except ValueError:
            print("Digite um código numérico válido.")

    while True:
        try:
            nome = input("Informe seu nome: ").strip()

            if len(nome) < 3:

                print("O nome deve possuir pelo menos três caracteres.")
                
            elif not nome.replace(" ", "").isalpha():
                print("Não é permitido números ou símbolos.")
            else:
                break 
                      
            print("O nome deve possuir pelo menos três caracteres.")

        except ValueError:
            print("não é permitido numeros")    


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
            
            cliente = selecionar_cliente()

            if cliente is not None:
                Fazer_pedido(cliente, lista_produtos)

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

        elif op == "5":
            if len(lista_produtos) == 0:
                print("Nenhum produto cadastrado.")

            else:
                print("\n========== PRODUTOS ==========")
                for produto in lista_produtos:
                    produto.exibir_produto()
                    print("----------------------------")

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
def produtos():

    produto1 = Refeicao("Hambúrguer", 25.00, 12, "grande")
    produto2 = Refeicao("Batata Frita", 12.00, 13, "medio")

    produto3 = Bebida("Refrigerante", 7.00, 7, 400)
    produto4 = Bebida("Refrigerante", 7.00, 9, 600)

    produto5 = Refeicao("Pizza", 60.00, 11, "grande")

    produto6 = Sobremesa("Pudim", 10.00, 20, "especial")

    return [produto1, produto2, produto3, produto4, produto5, produto6]

lista_produtos = produtos()
clientes = []
#clientes = cliente()

#RETIRADO para ser possivel cadastrar.
#def funcionarios ():
#
#   funcionario1 = Funcionario("eliandro", "12345678911", 123)
#    funcionario2 = Funcionario("vinicios", "12345678912", 132)
#    funcionario3 = Funcionario("sarah", "12345678913", 143)

#    return [funcionario1,funcionario2, funcionario3]

#def cliente():
#    cliente1 = Cliente(144, "dylan", "1234567899")
#    cliente2 = Cliente(154, "Heloa", "1234567898")
#    return [cliente1, cliente2]


if __name__ == "__main__":
    Sistema_principal()