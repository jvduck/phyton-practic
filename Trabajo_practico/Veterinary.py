class Veterinaria():
    
    def __init__(self) -> None:
        self.__listado = []
    
    def __str__(self) -> str:
        return f'En la veterianaria hay {len(self.__listado)} pacientes registrados'

    def setPaciente(self, paciente:str):
        self.__listado.append(paciente)
    
    def deletePaciente(self, paciente: str):
        self.__listado.remove(paciente)
    
    def getListado(self):
        print("listado: ")
        return self.__listado
            
class Animal(Veterinaria):
    
    
    def __init__(self, nombre:str, edad:int) -> None:
        super().__init__()
        self.__nombre = nombre
        self.__edad = edad
        
        
    def __str__(self) -> str:
        return f'El paciente se llama {self.__nombre} y tiene {self.__edad} años'
    
    
class Paciente(Animal):
    
    def __init__(self, nombre: str, edad: int, color:str, raza:str) -> None:
        super().__init__(nombre, edad)
        self.__raza = raza
        self.color = color
        self.__consultas = []
        self.__paciente_con_tratamiento = False
    
    def __str__(self) -> str:
        return f'{super().__str__()} Raza: {self.__raza} a venido a {len(self.__consultas)} consultas'


    def setConsulta(self, consulta):
        if self.__consultas.append(consulta):
            self.__paciente_con_tratamiento = True
        else:
            self.__paciente_con_tratamiento = False
    
    def getDatos(self):
        return f'Nombre: {self.__nombre}\nEdad: {self.__edad}\nRaza: {self.__raza}\nConsultas: {self.__consultas}\nPaciente con tratamiento médico: {self.__paciente_con_tratamiento}'
