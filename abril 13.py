#coleeciones: tuplas, listas , diccionarios

nombre="Sebastian"
edad=35
casado=False
mascota="Gamora"
ciudad="Mar del plata"
#indices  0     1    2       3      4
datos=(nombre,edad,casado,mascota,ciudad)

#indice: una ubicacion dentro de una tupla/lista, que nos indica la posicion en la que vamos a acceder a nuestros datos.
#estos indices son del tipo NUMERICOS. Estos indices ARRANCAN DEL VALOR 0

#print(datos[1])

#metodos para tuplas
#print(datos.count(edad)) #nos indica la cantidad de veces que se repite un dato que indiquemos nosotros

#print(datos.index("Gamora")) #nos indica en que indice se encuentra un dato. Si no se encuentra el dato en un indice ARROJARA UN ValueError (error de valor de indice, en este caso)

#print(len(datos)) #nos permite saber cual es el largo de nuestra tupla

alumno1=("Alexis","Programacion FullStack")
alumno2=("Yanina",("Inglés","Matematica"))
alumno3=("Bautista","Historia")
alumno4=("Ariel",("Programacion","Lengua","Geografia"))

academia=(alumno1,alumno2,alumno3,alumno4) 
#!indices                  0                              1                                  2                                3
#!sub-indices    0               1                  0               1                    0            1         0                     1
#!sub-indice2                                                  0           1                                                 0          1          2
#* academia=(("Alexis","Programacion FullStack"),("Yanina",("Inglés","MATEMATICA")),("Bautista","Historia"),("Ariel",("Programacion","Lengua","Geografia")))
#* print(academia[0]) #* A traves de los sub-indices, puedo acceder a informacion que se encuentre dentro de las tuplas ANIDADAS
#imprimir "MATEMATICA"
print(academia[1][1][1])

#imprimir programacion de ariel
print(academia[3][1][0])

#iprimir el nombre del alumno y su primer materia
print(f"El alumno {academia[3][0]} esta estudiando {academia[3][1][0]}")
