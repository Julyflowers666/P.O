from carro import Carro
from locadora import Locadora
from vendedor import Vendedor
from endereco import Endereco

vender1 = Vendedor (6, "julio", 19, 35346)
vender2 = Vendedor (8, "Lucaas", 22, 43654)
carro1 = Carro ("Volkswagen","fusca", 1986, 0)
carro2 = Carro ("Chevrolet","prisma", 2018, 50.000)
carro3 = Carro ("Chevrolet","Onix", 2024, 0)
endereco = Endereco ("cabral", 1420, "Aeroporto", "Corumba")

vendedores = [vender1,vender2]
carros = [carro1, carro2, carro3]
locadora = Locadora (1, vendedores, carros, endereco)

print(carro2)