from claseAuto import Automovil

#Almacenar mis objetos en un Garage. Va a ser una clase denominada Garaje, la cual, va a almacenar objetos de la clase Automovil

class Garage():
    
    def __init__(self,tamanio) -> None:
        self.tamanio = tamanio #cant de mts2 del garage
        self.capacidad_disponible = tamanio
        self.capacidad_ocupada = 0
        self.contenidos = []
        
    def __str__(self) -> str:
        return f'El garage tiene {self.tamanio} tamaño: {self.capacidad_disponible} se encuentra disponible ({self.capacidad_ocupada} ocupado). contiene {len(self.contenidos)} vehiculos'
        
    def recibirVehiculo(self,vehiculo,espacio):
        #comprobar que hay lugar
        if self.capacidad_disponible < espacio:
            print("No hay espacio para este vehiculo")
            return
        #aumentar capacidad ocupada
        #reducir espacio disponible
        self.capacidad_ocupada += espacio
        self.capacidad_disponible -= espacio
        #poner el objeto y espacio ocupado en el array de contenidos
        self.contenidos.append([vehiculo,espacio])
        print("Se agrego el Vehiculo al garage")
    
    def liberarVehiculo(self):
        #buscar en el array el vehiculo y quitarlo.
        for i in range(len(self.contenidos)):
            print(f'{i+1}) Vehiculo: {self.contenidos[i][0]} ,Tamaño: {self.contenidos[i][1]}')
        seleccion = int(input("Elija el Vehiculo a quitar: "))
        removido = self.contenidos.pop(seleccion-1) #guardamos el indice que se quito. (contiene el vehiculo y el espacio)
        #aumentar la cap disponible
        #reducir el espacio ocupado
        self.capacidad_ocupada -= removido[1]
        self.capacidad_disponible += removido[1]
        return removido[0]
        
garage1= Garage(40)

auto1 = Automovil("Ford","Mustang","Rojo",1981)
auto2 = Automovil("Chevrolet","Corvette","Blanco",1981)
print(auto1)

garage1.recibirVehiculo(auto1,6)
garage1.recibirVehiculo(auto2,8)

print(garage1)

vehiculo_liberado = garage1.liberarVehiculo()
print(f'Se quito al vehiculo {vehiculo_liberado}')

"""
crear Clase  que se llame Salon(). la clase salon tiene una capacidad de personas, (numerica), y cada objeto guardado, ocupa un lugar.
Salon tiene atributos de capacidad = numerica, nombre_curso = string , estado_completo = false , lista_alumnos = []

Usar la clase Salon para crear un salon de clases (programacion = Salon(xx,xx)), y tendra 2 metodos: agregar alumno y quitar alumno.
El atributo estado_completo , cambiara a true al momento que se llegue a la maxima capacidad. TIP: creen un atributo que les permita contabilizar la cant de gente que hay ocupando

por ultimo imprimir el objeto creado de Salon, que nos debe indicar "El salon de *nombre* tiene *cant* alumnos (espacio restante: *disponible*)
"""