from typing import Any


class Persona():
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        
        self.caminar = 0
        self.despierto = False
        self.arrancar = 0
        
        
    def __str__(self):
        caracteristicas = f'{self.nombre} {self.edad} {self.pais}'
        return caracteristicas
    
    def getDescripcion(self):
        return f'Me llamo {self.nombre}, tengo {self.edad} años, y soy {self.pais}'
    
    def getEstadopersona(self):
        if self.despierto == True:
            return "La persona esta despierta."
        else:
            return "La persona esta dormida."
    
    def setDespertar(self):
        if self.despierto == False:
            self.despierto = True
            return 'despertando persona'
        else:
            self.despierto = False
            return 'acostando persona'
    
    def setCaminar(self):
        if self.caminar > 0:
            return f'la persona se encuentra caminando a {self.caminar}km/h'
        else:
            return 'la persona esta quieta'
    
    def setArrancar(self,arranque):
        if self.despierto == True:
            self.caminar += arranque
        else:
            print("persona dormida, hay que despertarla")
    
    
persona1 = Persona("Juan", 26, "español")
persona2 = Persona("Martin", 32, "argentino")

id_perona1 = persona1.getDescripcion()
print(id_perona1)

id_perona2 = persona2.getDescripcion()
print(id_perona2)

estado_1 = persona1.getEstadopersona()
print(estado_1)

arriba = persona1.setDespertar()
print(arriba)
nuevoestado = persona1.getEstadopersona()
print(nuevoestado)

caminar = persona1.setCaminar()
print(caminar)
persona1.setArrancar(10)
print(persona1.setCaminar())