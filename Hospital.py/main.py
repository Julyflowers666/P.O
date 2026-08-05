from pacientes import Pacientes
from consulta import Consulta
from medico import Medico

def main():
    paciente1 = Pacientes(1,"josé",30,"masculino","134-213-152-00")
    medico1 = Medico(1,"dr.pavão","BW-MS 23542","Cardiologista")
    consulta1 = Consulta(1001,paciente1,medico1, "30/02/26", "16:00")

    paciente1.Mostrar_dados()
    medico1.Mostrar_dados()
    consulta1.Mostrar_dados()

    print("---CONFIRMAR CONSULTA---")
    consulta1.confirmar_consulta()

    medico1.Mostrar_dados

    paciente1.desativar()
    consulta1.confirmar_consulta()

    medico1.alterar_disp()
    consulta1.confirmar_consulta

if __name__ == "__main__":
    main()