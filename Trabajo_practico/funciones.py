from Veterinaria import Paciente

def nuevoPaciente():
    new_pet = Paciente()
    return new_pet

def deletePaciente(paciente):
    for i in range (len(paciente[i])):
        paciente.remove(i)
        print (f'Se elimino {paciente}')
        break

def listarPaciente(paciente):
    for i in paciente:
        print(f'pacientes: {i}')

def nuevaConsulta(paciente, consulta):
    paciente.consulta.append(consulta)
    

def obtenerDetallePaciente(paciente, consulta):
    print(f'El paciente {paciente.getDatos} tiene {len(consulta)} consultas')