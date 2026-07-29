from produto import Produto
from cliente import Cliente
from venda import Venda

def main():
    cliente1 = Cliente(1,"joão","134.242.255-00")
    produto1 = Produto("B001","teclado",150, 24)
    venda1 = Venda(cliente1,produto1, 2)

    cliente1.exibir_dados()
    produto1.Mostrar_dados()

    venda1.finaliza_venda()
    
    produto1.Mostrar_dados()

if __name__ == "__main__":
    main()