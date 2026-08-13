class Livro:
    def __init__(self,codigo,titulo,autor,disponivel):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = disponivel
    @property
    def get_codigo(self):
        return self.__codigo
    @property
    def get_titulo(self):
         return self.__titulo
    @property
    def get_autor(self):
        return self.__autor
    @property
    def get_disponivel(self):
         return self.__disponivel
    
    def mostrar_dados_livro(self):
        print("\n--- DADOS ---")
        print(f"Codigo: {self.__codigo}")
        print(f"Titulo: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Disponivel: {self.__disponivel}")
