class Consulta:
    def __init__(self,codigo,paciente,medico,data,horario,):
        self.codigo = codigo
        self.paciente = paciente
        self.medico = medico
        self.data = data
        self.status = "agendada"
        self.horario = horario

    
    def Mostrar_dados(self,):
        print("----Dados da consulta----")
        print(f"codigo: {self.codigo}")
        print(f"paciente: {self.paciente.nome}")
        print(f"medico: {self.medico.nome}")
        print(f"especialidade: {self.medico.setor}")
        print(f"data: {self.data}")
        print(f"horario: {self.horario}")
        print(f"status: {self.status}")

    def validar_consulta(self):
        if not self.paciente.ativo:
            print("consulta não pode ser agendada:paciente inativo")
            return False
        if not self.medico.disponivel:
            print("consulta não pode ser agendada: medico indisponivel")
            return True
        print("consulta validada com sucesso")
        return True

    def confirmar_consulta(self):
        if self.status == "cancelada":
            print("não é possivel confirmar uma consulta cancelada")
            return
        if self.status == "realizada":
            print("a consulta já foi realizada")
            return
        if self.validar_consulta():
            self.status = "confirmada"
            self.medico.disponivel = False
            print("consulta confirmada com sucesso")

    def cancelar_consulta(self):
        if self.status == "Cancelada":
            print("a consulta ja esta cancelada")
            return
        if self.status == "realizada":
            print("não é possivel cancelar uma consulta realizada")
            return

        self.status = "cancelada"
        self.medico.disponivel = True
        print("consulta cancelada com sucesso")

    def realizar_consulta(self):
        if self.status == "cancelada":
            print("não é possivel realizar uma consulta cacelada")
            return
        if self.status == "agendada":
            print("a consulta precisa ser confirmada antes")
            return
        if self.status == "realizada":
            print("a consulta ja foi realizada")
            return

        self.status = "realizada"
        self.medico.disponivel == True
        print("consulta realizada com sucesso")