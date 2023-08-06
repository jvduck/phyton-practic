'''
Crear la clase persona que contiene los atributos de nombre, apellido y DNI
de esta clase, crear 2 clases hijas: alumnos , profesores.
Alumnos tiene como atributo agregado, el anio que cursa (1ero, 2ero, 3ero, etc)
Profesores tiene como atributo, la materia que dicta.

Luego crearemos la clase Curso: el cual tendra como atributos la materia (string), profesor: sera una instancia creada desde la clase Profesores, y tendra alumnos, que seran instacias de la clase alumnos (sera una lista que los contendra)
'''

class Persona():
    def __init__(self,nombre: str,apellido: str, dni: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        
    def __str__(self) -> str:
        return f'{self.__apellido},{ self.__nombre} DNI:{self.__dni}'
    
class Alumnos(Persona):
    def __init__(self, nombre: str, apellido: str, dni: str,cursada: str) -> None:
        super().__init__(nombre, apellido, dni)
        self.__cursada =  cursada

    def __str__(self) -> str:
        return f'{super().__str__()}, Curso:{self.__cursada}'
    
class Profesores(Persona):
    def __init__(self, nombre: str, apellido: str, dni: str, materia: str) -> None:
        super().__init__(nombre, apellido, dni)
        self.__materia = materia
        
    def __str__(self) -> str:
        return f'{super().__str__()}, Materia:{self.__materia}'
    
class Curso():
    
    def __init__(self) -> None:
        self.__materia = ''
        self.__profesor = ''
        self.__alumnos = []
        
    def __str__(self) -> str:
        return f'Materia: {self.__materia}, Profesor: {self.__profesor}. Cant Alumnos: {len(self.__alumnos)}'
    
    def setCurso(self,materia: str):
        self.__materia = materia
        
    def setProfesor(self,profesor: str):
        self.__profesor = profesor
    
    def setAlumnos(self,alumno):
        self.__alumnos.append(alumno)
        
    def getAlumnos(self):
        print('Los alumnos son:')
        for alumno in self.__alumnos:
            print(alumno)
