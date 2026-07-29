class Pacientes:
    def __init__(self,nome,idade,genero,cpf):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cpf = cpf
        
    def Mostrar_dados(self):
        print("----Dados----")
        print(f"Nome do paciente: {self.nome}")
        print(f"idade do paciente: {self.idade}")
        print(f"genero: {self.genero}")
        print(f"cpf: {self.cpf}")