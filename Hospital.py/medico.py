class Medico:
    def __init__(self,codigo,nome,crm,setor):
        self.codigo = codigo
        self.nome = nome
        self.crm = crm
        self.setor = setor
        self.disponivel = True
        
    def Mostrar_dados(self):
        print("----Dados----")
        print(f"codigo:{self.codigo}")
        print(f"nome do medico: {self.nome}")
        print(f"crm: {self.crm}")
        print(f"setor: {self.setor}")
        print(f"disponibilidade: " f"{'disponivel' if self.disponivel else 'indisponivel'}")

    def alterar_disp(self):
        self.disponivel = not self.disponivel

        if self.disponivel:
            print(f"medico {self.nome} agora esta disponivel")
        else:
            print(f"medico {self.nome} agora está indisponivel")