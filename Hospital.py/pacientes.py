class Pacientes:
    def __init__(self, codigo,nome,idade,genero,cpf):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cpf = cpf
        self.ativo = True
        
    def Mostrar_dados(self):
        print("----Dados----")
        print(f"Nome do paciente: {self.nome}")
        print(f"idade do paciente: {self.idade}")
        print(f"genero: {self.genero}")
        print(f"cpf: {self.cpf}")
        print(f"situação: {'ativo' if self.ativo else 'inativo'}")

    def desativar(self):
        if not self.ativo:
            print(f"paciente {self.nome} desativado com sucesso")

    def ativo(self):
        if self.ativo:
            print("o pciente ja esta ativo")
        else:
            self.ativo = True
            print(f"paciente {self.nome} ativado com sucesso")