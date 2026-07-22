from pagamentos import Pagamentos
from produto import Produtos
from cliente import Cliente

produto1 = Produtos ("5235", "Livro", 50, 120, "Livros")
produto2 = Produtos ("6874", "brinco", 45, 89, "Acessorio")
produto3 = Produtos ("3468", "boneca", 20, 12, "Brinquedo")
cliente1 = Cliente ("Junior", "jr.Email")
cliente1 = Cliente ("vinicios", "viny.Email")
Formas = Pagamentos ("Numero ou cpf", "debito ou credito", "sla1 ou sla2")

print (cliente1)
print (produto1)