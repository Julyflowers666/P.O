class Medico:
    def __init__(self,nome,cnpj,setor,):
        self.nome = nome
        self.cnpj = cnpj
        self.setor = setor
        
    def Mostrar_dados(self):
        print("----Dados----")
        print(f"nome do medico: {self.nome}")
        print(f"cnpj: {self.cnpj}")
        print(f"setor: {self.setor}")