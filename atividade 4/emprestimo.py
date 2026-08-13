from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from livro import Livro

class Emprestimo (Pessoa, Livro):
    def __init__(self, nome, cpf, codigo, dias, status):
        super().__init__(nome, cpf)
        self.__codigo = codigo
        self.__dias = dias
        self.__status = status

    def mostrar_dados(self):
        print("\n--- DADOS ---")
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")
        print(f"codigo: {self.__codigo}")
        print(f"livro: {self.__livro}")
        print(f"Dias: {self.__dias}")
        print(f"Status: {self.__status}")

aluno1 = Aluno ("Joao","12345678911","1234567","tec.enfermagem")
professor1 = Professor ("Luiz", "21345678911", "12345","enfermagem")

aluno1.mostrar_dados_aluno()
professor1.mostrar_dados_professor()