class Test ():
    def __init__(self,valor):
        self.x = valor

    def get_valor (self):
        return self.x

    def set_valor(self,v):
        self.x = v

test = Test (10)
print("valor do objeto", test.get_valor())

val = int(input("digite um novo valor: "))
test.set_valor(val)
print("novo valor do objeto:", test.get_valor())