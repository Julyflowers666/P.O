from pessoa import Pessoa

class Pacientes (Pessoa):
    def __init__(self, nome, cpf, telefone, endereco, idade, convenio):
        super().__init__(nome, cpf, telefone, endereco)
#super é para pegar o construtor mãe para a class filho
        self.idade = idade
        self.convenio = convenio

    def exibir_paciente(self):
        
        self.apresentar()
        print(f"idade: {self.idade}")
        print(f"convenio {self.convenio}")