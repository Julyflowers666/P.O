from pacientes import Pacientes
from medico import Medico

paciente1 = Pacientes("josé","134-213-152-00","(55) 925423-23525", "america",35,"unimed")
medico1 = Medico("dr.pavão","867-235-786-00","(55) 958456-72465","frei mariano","93568743","Clinico Geral")

print("-----paciente---")
paciente1.exibir_paciente()

print("------medico-----")
medico1.exibir_medico()

