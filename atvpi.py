class Alerta:
    def __init__(self,local, nivel, fwi, temp, umi, vent):
        self.local = local
        self.nivel = nivel
        self.fwi = fwi
        self.temp = temp
        self.umi = umi
        self.vent = vent

    def dados(self):
        print(f"o local: {self.local}")
        print(f"está com o nivel em estado: {self.nivel}")
        print(f"o indice meteorologico de incedio é: {self.fwi}")
        print(f"a temperatura está em: {self.temp}°c")
        print(f"umidade do local: {self.umi}%")
        print(f"o vento em km/h: {self.vent}")

inf1 = Alerta ("serrado", "Critico", 38.6, 41.2, 12, 24.5 )

inf1.dados()