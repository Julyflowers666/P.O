class aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def apresentar(self):
        print(f"ola, meu nome é {self.nome}")
        print(f"tenho {self.idade} anos")
        print(f"a minha matricula é {self.matricula}")

info1 = aluno("joão", 20, 2520324)
info2 = aluno("maria", 19, 5468483)

info2.apresentar()