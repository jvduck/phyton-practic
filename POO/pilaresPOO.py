""" 
PILARES:
Herencia:
Encapsulamiento:
Abstraccion:
Polimorfismo:

"""

#? ABSTRACCION: Debemos ocultar informacion la cual no sea relevante para el uso del programa, al momento que debamos identificar un objeto:

class Mascota():
    
    def __init__(self,nombre,edad,raza,peso,color) -> None:
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
        self.peso=peso
        self.color=color
        
    def __str__(self) -> str:
        return f'{self.nombre}'
    

mascota1 = Mascota("Firulais",5,"Border Collie",25,"Negro y blanco")
#print(mascota1)


#? Encapsulamiento: consiste en PROTEGER LA INFORMACION que contengan nuestros objetos, y evitar que puedan ser alterados, excepto por un metodo que lo permita. Para encapsular un atributo, simplemente le colocamos los doble guion bajo __

class Auto():
    def __init__(self,color) -> None:
        self.__color = color
        
    def setColor(self,color):
        self.__color = color
        
    def __str__(self) -> str:
        return f'Su color es {self.__color}'
    
auto1 = Auto("Verde")
auto1.setColor("Azul")
print(auto1)
auto1.__color = "Violeta" #! NO SE DEBE PODER CAMBIAR ATRIBUTOS DESDE EL EXTERIOR DE LA CLASE
print(auto1)

#Herencia: Permitir que una clase, tome los atributos y metodos de otra. Esto permite "heredar" caracteristicas y comportamientos

class Vehiculo():
    
    def __init__(self,marca,modelo,color) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def __str__(self) -> str:
        return f'{self.marca} {self.modelo}'
    
    def darArranque(self):
        print("Arrancando el vehiculo")
        

class Auto(Vehiculo):
    
    def __init__(self, marca, modelo, color, puertas) -> None:
        super().__init__(marca, modelo, color)
        self.puertas = puertas
        
    def __str__(self) -> str:
        return f'{super().__str__()} {self.puertas} puertas'

class Moto(Vehiculo):
    
    def __init__(self, marca, modelo, color,cilindrada) -> None:
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada


mi_auto = Auto("ford","mustang","verde",5)
mi_moto = Moto("Harley","1100RTC","Gris",1100)

print(mi_auto)
print(mi_moto)

#Polimorfismo: Es la capacidad que tiene un objeto, de interactuar de manera distinta, segun sus atributos.
#ej: crearemos 3 personas, las cuales Saludaran en 3 idiomas distintos

class Persona():
    def __init__(self,nacionalidad) -> None:
        self.nacionalidad = nacionalidad
    
    def saludar(self):
        print(f'{self.saludo}')

class Argentino(Persona):
    def __init__(self, nacionalidad,saludo) -> None:
        super().__init__(nacionalidad)
        self.saludo = saludo
        
class Ingles(Persona):
    def __init__(self, nacionalidad,saludo) -> None:
        super().__init__(nacionalidad)
        self.saludo = saludo
        
class Italiano(Persona):
    def __init__(self, nacionalidad,saludo) -> None:
        super().__init__(nacionalidad)
        self.saludo = saludo
        
argen1=Argentino("Argentina","Que onda pa")
argen1.saludar()
ingles1=Ingles("Inglaterra","Hello there")
ingles1.saludar()

""" 

crear la Clase Estudiante y la Clase Profesor. Estos heredaran las caracteristicas de una Clase superior llama Persona (contiene nombre, apellido y dni). La clase Estudiante tendra ademas un atributo que indica el año que cursa. La Clase Profesor tendra un atributo que indica la materia que dicta.

crear el STR en todas las clases, y que indique nombre y apellido, y en Estudiante ademas, indicar que año cursa.

Recordar poner TODOS SUS ATRIBUTOS ENCAPSULADOS 

"""