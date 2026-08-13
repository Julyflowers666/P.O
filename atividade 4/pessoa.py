class Pessoa:
    def __init__(self,nome,cpf):
        self.__nome = nome
        self.__cpf = cpf
    @property
    def get_nome(self):
        return self.__nome
    @property
    def get_cpf(self):
         return self.__cpf
    @property
    def set_cpf(self, cpf):
            
            cpf_limpo = cpf.replace(".", "").replace("-", "").strip()
    
            if not cpf_limpo.isdigit() or len(cpf_limpo) != 11:
                print("Erro: o CPF deve possuir exatamente 11 números.")
                return False
    
            self.__cpf = cpf_limpo
            return True

    def mostrar_dados(self):
        print("\n--- DADOS ---")
        print(f"Nome: {self.__nome}")
        print(f"CPF: {self.__cpf}")
