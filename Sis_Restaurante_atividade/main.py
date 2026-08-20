from bebida import Bebida
from cliente import Cliente
from pedido import Pedidos
from produto import Produto
from refeicao import Refeicao
from sobremesa import Sobremesa

def cadastrar_cliente():
    while True:
        try:
            codigo = int(input("Informe o seu código: "))
            break
        except ValueError:
            print("Digite um código numérico válido.")

    # Validação do nome antes de criar o objeto.
    while True:
        nome = input("Informe seu nome: ").strip()

        if len(nome) >= 3:
            break

        print("O nome deve possuir pelo menos três caracteres.")

    while True:
            
            telefone = int(input("Informe o telefone: "))


            return Cliente(codigo, nome, telefone)
                
def main():

    print("====================================")
    print("   SISTEMA DE PEDIDOS DE RESTAURANTE      ")
    print("====================================")

    cadastrar_cliente()

if __name__ == "__main__":
    main()