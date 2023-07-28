class Automovil():
    def __init__(self, marca, modelo, color, anio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        
        self.encendido = False
        self.velocidad = 0
        self.aceleracion = 0
        
    def __str__(self):
        caracteristicas = f'{self.marca} {self.modelo}'
        return caracteristicas
    
    def getDescripcion(self):
        return f'Este auto es un {self.marca}, modelo {self.modelo}, color {self.color} del año {self.anio}'
    
    
    def getEstado(self):
        if self.encendido == True:
            return "El auto esta encendido"
        else:
            return "El auto se encuentra apagado"
        
        
    def setEncendido(self):
        if self.encendido == False:
            self.encendido = True
            return 'Arrancando vehiculo'
        else:
            self.encendido = False
            return 'Vehiculo detenido'
        
        
    def getVelocidad(self):
        if self.velocidad > 0:
            return f'Vehiculo en movimiento, a {self.velocidad}Km/h'
        else:
            return 'Vehiculo sin movimiento'
        
        
    def setAcelerar(self,aceleracion):
        if self.encendido == True:
            self.velocidad += aceleracion
        else:
            print("Vehiculo apagado, poner en marcha")
            
            
            
    def setFrenar(self,frenado):
        if self.encendido == False:
            print("El vehiculo esta apagado")
            return
        elif self.velocidad == 0:
            print("Auto detenido")
            return
        elif self.velocidad <= frenado:
            self.velocidad = 0
            return
        elif self.velocidad > frenado:
            self.velocidad -= frenado
            return
    
    
car1 = Automovil("Ford","Focus", "negro",2022)
car2 = Automovil("Chevrolet","Corvette","Blanco", 2018)
    
descripcion_car = car1.getDescripcion()
print(descripcion_car)

descripcion_car = car2.getDescripcion()
print(descripcion_car)
    
estado1 = car1.getEstado()
print(estado1)

encendido1 = car1.setEncendido()
print(encendido1)

estado_new =car1.getEstado()    
print(estado_new)

velocidad = car1.getVelocidad()
print(velocidad)

print(car1.getVelocidad())
car1.setAcelerar(40)
print(car1.getVelocidad())
car1.setAcelerar(60)
print(car1.getVelocidad())
car1.setFrenar(20)
print(car1.getVelocidad())