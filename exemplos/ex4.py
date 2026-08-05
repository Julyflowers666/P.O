class ContaBancaria():
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    def get_saldo(self):
        return self.__saldo

    def set_depositar(self,valor):
        if valor > 0:
            self.__saldo = valor
            print(f"O valor de R$ {valor} foi depositado na conta")
        else:
            print("o valor não pode ser menor que zero!")

conta = ContaBancaria("july", 300)
print(f"Titular da conta: {conta.titular}")
print(f"saldo da conta: {conta.get_saldo()}")
#só acessa com get
conta.set_depositar(2000)
print(f"novo saldo da conta: {conta.get_saldo()}")