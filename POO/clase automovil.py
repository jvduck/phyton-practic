#Creacion de una clase: las clases se crear !!!!CAPITALIZADAS!!!!!

class Automovil():
    #comenzar a definir un estado inicial de mi objeto:
    def __init__(self,marca,modelo,color,fabricacion):
        #estos son los ATRIBUTOS iniciales
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.fabricacion = fabricacion
        #estos atributos hacen referencia a ESTADOS INICIALES que vamos a cambiar
        self.encendido = False #significa que esta apagado
        self.velocidad = 0 #no esta en movimiento o a que velocidad se mueve
        self.acelerar = 0 #me va a generar un movimiento en el auto
        
    #metodo magico __str__ para conocer mas caracteristicas sobre un objeto
    def __str__(self):
        caracteristicas = f'{self.marca} {self.modelo}'
        return caracteristicas
    
    #GET-SET (estan van a ser nuestras maneras de poder identificr ACCIONES que vamos a ejecutar en un objeto)
    
    def getCaracteriscas(self): #para OBTENER INFORMACION
        return f'Este vehiculo es un {self.marca} , modelo {self.modelo}, color: {self.color}, del año {self.fabricacion}'
    
    def getEstadoEncendido(self): #ve si el auto esta encendido o no
        #veremos los estados de mi atributo encendido
        if self.encendido == True:
            return "El vehiculo se encuentra encendido."
        else:
            return "El vehiculo esta apagado."
            
            
    def setEncendido(self): #PARA ENVIAR ALGUNA INFORMACION U MODIFICAR ATRIBUTOS
        #cambiaremos los estados de mi atributo encendido
        if self.encendido == False:
            self.encendido = True
            return 'Arrancando el Vehiculo'
        else:
            self.encendido = False
            return 'Deteniendo el vehiculo'
    
    def getVelocidad(self):
        if self.velocidad > 0:
            return f'El vehiculo se encuentra moviendose a {self.velocidad}km/h '
        else:
            return 'El vehiculo no se encuentra en movimiento'
        
    def setAcelerar(self,aceleracion):
        if self.encendido == True:
            self.velocidad += aceleracion
        else:
            print("Vehiculo apagado. Por favor , encienda el vehiculo")

    def setFrenar(self,frenado):
        #EVALUAR LOS CASOS FALSOS , POR SOBRE LOS VERDADEROS
        
        if self.encendido == False:
            print("El Vehiculo esta apagado.")
            return
        elif self.velocidad == 0:
            print("El auto esta detenido")
            return
        elif self.velocidad <= frenado:
            self.velocidad = 0
            return
        
        elif self.velocidad > frenado:
            self.velocidad -= frenado
            return

        
     
mi_auto = Automovil("Ford","Mustang","Verde",1966)
mi_auto2 = Automovil("Chevrolet","Corvette","Blanco",1969)

#para usar un metodo , debemos LLAMAR AL OBJETO y LLAMAR A SU METODO:

caracteriscas_objeto = mi_auto.getCaracteriscas()
# print(caracteriscas_objeto)

# caract_objeto2 = mi_auto2.getCaracteriscas()
# print(caract_objeto2)

# estado_1 = mi_auto.getEstadoEncendido()
# print(estado_1) #vemos el estado inicial del encendido
# accion = mi_auto.setEncendido() #ejecuto un metodo que me cambia el estado del encendido
# print(accion) #vemos lo que me devolvio ese estado
# nuevo_estado = mi_auto.getEstadoEncendido()
# print(nuevo_estado) #verificamos ahora como estaria mi encendido

# # velocidad = mi_auto.getVelocidad()
# # print(velocidad)

# print(mi_auto.getVelocidad()) #INICIAL : 0
# mi_auto.setAcelerar(30)
# print(mi_auto.getVelocidad()) # => 30
# mi_auto.setAcelerar(50)
# print(mi_auto.getVelocidad()) # => 80
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad()) # => 60
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad()) # => 60
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad()) # => 60
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad()) # => 60
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad()) # => 60
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad()) # => 60
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad()) # => 60
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad()) # => 60
# print(mi_auto.velocidad)

#CASO EJEMPLO

# accion = mi_auto.setEncendido() #ejecuto un metodo que me cambia el estado del encendido
# print(accion) #vemos lo que me devolvio ese estado


# print(mi_auto.getVelocidad()) #VEMOS LA VELOCIDAD
# mi_auto.setAcelerar(50) 
# print(mi_auto.getVelocidad())

# estado_2 = mi_auto.setEncendido()
# print(estado_2)
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad())
# mi_auto.setAcelerar(50) 
# mi_auto.setFrenar(20)
# print(mi_auto.getVelocidad())
# mi_auto.setFrenar(20)
# mi_auto.setFrenar(20)
# mi_auto.setFrenar(20)

"""
Van a crear la clase Persona. Esta clase tiene de atributos iniciales: nombre, edad, nacionalidad , y como estados tiene caminar (estado valor 0), despierto (true)

el metodo str va a devolver lo siguiente: Me llamo *nombre*, tengo *edad* y soy *nacionalidad* => "Me llamo Seba, tengo 36, y soy argentino"

luego instancien 2 personas totalmente distintas. Muestren con un print del objeto, para asegurarse que devuelva de manera correcta el metodo magico con el mensaje que le creamos

"""

"""
vamos a poner metodos del tipo get-set:
la persona puede caminar o frenar mientras camina. Debemos tener un metodo que nos diga si la persona esta caminando, y a cuanto. Y metodos para que avance o se detenga
luego, un metodo que la persona vaya a dormir o la va a despertar (setear el estado de despierto.) 

*Posibilidad 1:
si la persona NO ESTA DESPIERTA (se encuentra dormido), no podra caminar. 

*Posibilidad 2:
agregar un nuevo atributo que sea "sonambulo". Y si la persona esta dormida, y su velocidad al caminar aumenta, cambiaremos este atributo a True, y pondremos que "la persona esta sonambula"
OJO: al momento de DESPERTAR  a la persona, este atributo DEBE CAMBIAR A FALSE

"""