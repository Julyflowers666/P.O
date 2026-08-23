from bebida import Bebida
from cliente import Cliente
from funcionario import Funcionario
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
            nome = input("Informe seu nome: ").strip()
            
            if len(nome) >= 3:
                break
            print("O nome deve possuir pelo menos três caracteres.")

    return Funcionario (nome,codigo)

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
    while True:
        print("--------- MENU ----------")
        print("1- Cadastrar Cliente")
        print("2- Cadastrar Funcionario")
        print("3- Cadastrar produto")
        print("4- Listar produtos")
        print("0- Sair")

        op = input("Escolha uma opção: ")

        if op == "1":
            cadastrar_funcionario()
        elif op == "2":
            cadastrar_cliente()
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

def main():

    print("------------------------------")
    print("   SISTEMA DE PEDIDOS DE RESTAURANTE      ")
    print("------------------------------")


if __name__ == "__main__":
    main()