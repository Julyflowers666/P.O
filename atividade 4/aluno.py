from pessoa import Pessoa

class Aluno (Pessoa):
    def __init__(self, nome, cpf, matricula, curso):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        self.__curso = curso
    @property
    def get_matricula(self):
        return self.__matricula
    @property
    def get_nome(self):
         return self.__nome
    @property
    def get_cpf(self):
        return self.__cpf
    @property
    def get_curso(self):
         return self.__curso

    def mostrar_dados_aluno(self):

            self.mostrar_dados()
            print(f"Matricula: {self.__matricula}")
            print(f"Curso: {self.__curso}")
                        