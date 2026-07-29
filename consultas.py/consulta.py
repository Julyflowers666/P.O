class Consulta:
    def __init__(self,data,setor,emergencia,preco):
        self.data = data
        self.setor = setor
        self.emergencia = emergencia
        self.preco = preco
    
    def Mostrar_dados(self,):
        print("----Dados----")
        print(f"paciente: {self.paciente.nome}")
        print(f"Dia da Consulta: {self.data}")
        print(f"tipo da Consulta: {self.setor}")
        print(f"Preferencia: {self.emergencia}")
        print(f"preço: {self.preco}")
