from bebida import Bebida
from cliente import Cliente
from pedido import Pedidos
from produto import Produto
from refeicao import Refeicao
from sobremesa import Sobremesa

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
# Remove espaços ou caracteres especiais, se quiser
            telefone_limpo = "".join(filter(str.isdigit, telefone))
# Verifica se o tamanho tem 10 ou 11 dígitos (ex: 11988887777)
            if len(telefone_limpo) == 11 or len(telefone_limpo) == 10:
                print("Telefone válido!")
            else:
                print("Telefone inválido. Digite o número com DDD.")
                return cadastrar_cliente()

            return Cliente(codigo, nome, telefone)


def main():

    print("====================================")
    print("   SISTEMA DE PEDIDOS DE RESTAURANTE      ")
    print("====================================")

    cadastrar_cliente()

if __name__ == "__main__":
    main()