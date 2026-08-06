from cliente import Cliente
from carro import Carro
from moto import Moto
from aluguel import Aluguel

def cadastrar_cliente():
    print("\n --- Cadastro do Cliente---")

    while True:
        try:
            codigo = int(input("infrome o codigo do cliente: "))
            break
        except ValueError:
            print("digite um codigo numerico")

        while True:
            nome = input("informe o nome do cliente: ")
            if len(nome.strip()) >= 3:
                break
            print("o nome deve possuir pelo menos tres caracteres")

        while True:
            cpf = input("informe o cpf com 11 numeros: ")
            cpf_limpo = cpf.replace(".", "").replace("-","").strip()
            if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
                break
            print("cpf invalido. informe extamente os 11 numeros")

        return Cliente(codigo,nome,cpf)

def cadastrar_veiculos():
    carro1 = Carro (1,"Volskvagem","fusca","2018",300.00,2)
    carro2 = Carro (2,"fiat","Uno","2014", 100.00,4)
    moto1 = Moto (3,"Honda","cg 160","2019",50.00,160)
    moto2 = Moto (4,"Kawasaki","Rh2","2020", 250.00,850)

    return [carro1, carro2, moto1, moto2]

def lista_veiculos(veiculos):
    print("\n --- Veiculos cadastrado ---")
    for veiculos in veiculos:
        print("\n---------------")
        veiculos.exibir_dados()

def buscar_veiculos(veiculos, codigo):
    for veiculos in veiculos:
        if veiculos.codigo == codigo:
            return veiculos
    return None        

def solicitar_quantidade_dia():
    while True:
        try:
            quantidade = int(input("informe a quantidade de dias: "))
            if quantidade > 0:
                return quantidade
            print("a quantidade deve ser maior que zero")
        except ValueError:
            print("digite somente numeros inteiros")

def main ():
    print("\n--- sitema de locação ---")
    cliente = cadastrar_cliente()
    veiculos = cadastrar_veiculos()
    lista_veiculos(veiculos)

    while True:
        try:
            codigo_veiculo = int(input("\n Digite o codigo do veiculo desejado: "))
        except ValueError:
            print("digite um codigo numerico")
            continue

        veiculos_escolhido = buscar_veiculos(veiculos, codigo_veiculo)

        if veiculos_escolhido in None:
            print("veiculo não encontrado")
            continue
        if not veiculos_escolhido.esta_disponivel():
            print("este veiculo não esta disponivel")
            continue
        break

    quantidade_Dias = solicitar_quantidade_dia()

    aluguel = aluguel(1,cliente,veiculos_escolhido,quantidade_Dias)

    if aluguel.finalizar():
        aluguel.exibir_resumo()

    print("\n situação atual do veiculo:")
    veiculos_escolhido.exibir_dados()


if __name__ == "__main__":
    main()