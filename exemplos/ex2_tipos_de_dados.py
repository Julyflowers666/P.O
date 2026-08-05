class Pessoa():
    def __init__(self,nome,idade,peso):
        self.nome = nome #Publico
        self._idade = idade #Protegido
        self.__peso = peso #Privado

pessoa = Pessoa("Flores", 20, 60)

print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa._idade}")
print(f"Peso: {pessoa.__peso}")
#Só é possivel acessar esse dados Dentro da Class