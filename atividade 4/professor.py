from pessoa import Pessoa

class Professor (Pessoa):
    def __init__(self, nome, cpf, registro, departamento):
        super().__init__(nome, cpf)
        self.__registro = registro
        self.__departamento = departamento

    def get_registro(self):
        return self.__registro

    def get_departamento(self):
        return self.__departamento
    
    def mostrar_dados_professor(self):
            
            self.mostrar_dados()
            print(f"Registro: {self.__registro}")
            print(f"Departamento: {self.__departamento}")