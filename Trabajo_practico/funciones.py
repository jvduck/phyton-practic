from Veterinary import Paciente

def nuevoPaciente():
    paciente = Paciente()
    return paciente

def deletePaciente(paciente):
    for i in range (len(paciente[i])):
        paciente.remove(i)
        print (f'Se elimino {paciente}')
        break

def listarPaciente(Veterinaria):
    pacientes = Veterinaria.getListado()
    if not pacientes:
        print("no hay pacientes registrados aún")
    else:
        for paciente in pacientes:
            print(paciente)

def nuevaConsulta(paciente, consulta):
    paciente.setConsulta(consulta)
    

def obtenerDetallePaciente(paciente, consulta):
    return print(f'El paciente {paciente.getDatos} tiene {len(consulta)} consultas')