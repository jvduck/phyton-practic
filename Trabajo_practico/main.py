from funciones import listarPaciente, obtenerDetallePaciente, nuevoPaciente, deletePaciente, nuevaConsulta
from Veterinaria import Paciente,Veterinaria,Animal

def progPrincipal():
    print("Bienvenido al sistema de gestion de la veterinaria")
    
    while True:
        print()
        opcion = int(input("Elija opción:\n1)Ver lista de pacientes\n2)Detalles del paciente a elección\n3)Cargar paciente nuevo\n4)Eliminar paciente: \n5)cargar consulta\n6)Dar de alta tratamiento médico\n7)Salir"))

        if opcion == 1:
            listarPaciente()
        elif opcion == 2:
            obtenerDetallePaciente()
        elif opcion == 3:
            nombre = input("nombre del paciente: ")
            edad = input("Edad: ")
            raza = input("Raza: ")
            paciente = Paciente(nombre, edad, raza)
            nuevoPaciente(paciente)
        elif opcion == 4:
            deletePaciente()
        elif opcion == 5:
            nuevaConsulta()
        elif opcion == 6:
            
            Paciente.setConsulta()
        elif opcion == 7:
            print("gracias por usar nuestro programa")
            break
        else:
            print("Opción no válida")
        continue

progPrincipal()

