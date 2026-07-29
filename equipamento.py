class Equipamento:
    def __init__(self,patrimonio,descricao,setor,situacao):
        self.patrimonio = patrimonio
        self.descricao = descricao
        self.setor = setor
        self.situacao = situacao

    def exibir_dados(self):
        print("\n -----Dados------")
        print (f"patrimonio: {self.patrimonio}")
        print (f"Descrição: {self.descricao}")
        print (f"setor: {self.setor}")
        print (f"situação: {self.situacao}")

    def alterar_situacao(self,nova_situacao):
        self.situacao = nova_situacao
        print(f"a situação foi alterada para {self.situacao}")

    def transferir_setor(self,novo_setor):
        self.setor = novo_setor
        print(f"equipamento transferido para o setor {self.setor}")

equipamento1 = Equipamento("BM-001","notebook dell","financeiro","Disponivel")
equipamento2 = Equipamento("CW-002","impressora Hp","Recursos Humanos","Em manutenção")

equipamento1.exibir_dados()
equipamento2.exibir_dados()

equipamento1.alterar_situacao("não disponivel")

equipamento2.transferir_setor("diretoria")
equipamento2.alterar_situacao("Disponivel")