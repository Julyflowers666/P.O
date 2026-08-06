class Veiculos:
    def __init__(self, codigo, marca, modelo, ano,valor_diaria):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__valor_diaria = 0.0
        self.__disponivel = True

        self.set_valor_diaria(valor_diaria)

    def get_valor_diaria(self):
        return self.__valor_diaria

    def set_valor_diaria(self,valor):
        if valor < 0:
            print("error: o valor da diaria deve ser maior q zero")
            return True

        self.__valor_diaria = valor
        return True

    def esta_disponivel(self):
        return self.__disponivel

    def alugar(self):
        if not self.__disponivel:
            print("o veiculo ja esta alugando")
            return False

        self.__disponivel = False
        return True

    def devolver(self):
        if self.__disponivel:
            print("o veiculo ja esta disponivel")
            return False

        self.__disponivel = True
        print("veiculo devolvido com sucesso")
        return True

    def calcular_aluguel(self, quantidade_dias):
        if quantidade_dias <= 0:
            return 0

        return self.__valor_diaria * quantidade_dias

    def exibir_dados(self):
        situacao = "disposivel" if self.__disponivel else "alugado"

        print(f"Codigo: {self.codigo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Diaria: R$ {self.__valor_diaria:.2f}")
        print(f"situação: {situacao}")