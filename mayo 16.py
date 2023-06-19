#? RETURN: nso permite OBTENER  algun tipo de valor derivado de la ejecucion de mi funcion:

#* def que calcula un promedio. Ese promedio luego, lo usaremos para verificar mediante un IF, si un alumno aprobo
"""
def calcularPromedio(not1,not2,not3):
    resultado=(not1+not2+not3)/3
    return resultado
    

nota1=8
nota2=6
nota3=4

promedio = calcularPromedio(nota1,nota2,nota3)

if promedio >= 4:
    print(f"Alumno aprobado. Nota: {promedio}")



def saludo():
    print(f"Hola {nombre}")


nombre = "Sebastian"
saludo()


def contenido():
    global nombre
    nombre = 'Seba'
    return nombre

#contenido() #en la linea 33, defino nombre globalmente como 'Seba'
nombre = 'Leandro' # aqui redefino 'Seba' como 'Leandro'
print(contenido())
print(nombre)

"""

#TODO: voy a recibir a traves del usuario un numero que me servira como parametro para ejecutar mi codigo: Este numero sera la cantidad de veces que se va a repetir un codigo, el cual me permitira agregar elementos a una lista de compras.


#*numero = int(input("Ingrese una cant de art a comprar:\n>>>"))

#*lista_compras = [] #El objetivo final es ENTREGAR UNA LISTA DE COMPRAS.

#for i in range(numero): #nos permite ejecutar el codigo una cant de veces determinada
#    articulo = input("Ingrese el art a comprar:")
#    lista_compras.append(articulo)

#! INCLUYAMOSLO DENTRO DE UNA FUNCION
"""""

def compras():
    lista_compras = [] #!CREAR ELEMENTOS DENTRO DE UNA FUNCION
    numero = int(input("Ingrese una cant de art a comprar:\n>>>"))
    for i in range(numero): #nos permite ejecutar el codigo una cant de veces determinada
        articulo = input("Ingrese el art a comprar: ")
        lista_compras.append(articulo)
    return lista_compras

lunes = compras()
martes = compras()

print(f
    Lunes: {lunes}
    Martes: {martes}
    


TODO: vamos a practicar la creacion de elementos en una funcion. Nuestra funcion ejecuta el sig codigo: se le va a pedir al usuario, que indique la cant de alumnos a ingresar. Luego, con un bucle (while/for) vamos a repetir un codigo que va a pedirle al usuario lo siguiente: nombre del alumno y materia. esto, se va a guardar en un DICCIONARIO, bajo las llaves de "Alumno" y "Materia". Ese diccionario, sera devuelto por la funcion, y lo almacenaremos en una variable.

!debemos ejecutar por lo menos 2 veces la funcion, y que los alumnos se guarden distinto

ej:

alumno1 = cargarAlumno()
alumno2 = cargarAlumno()

print(f"Alumno 1: {alumno1}, Alumno 2: {alumno2}")
SALIDA:
? 'Alumno 1: {"Nombre":"Seba","Materia","Programacion"}, Alumno 2: {"Nombre":"alejandro","Materia","Geografia"}

"""

lista= []
    
def registro(): #? REALIZA LA CARGA DE MANERA CORRECTA!!! Carga UN ALUMNO, y lo devuelve
    datos = {}
    nombre = input("Ingrese el nombre del alumno: ")
    materia = input("Ingrese el nombre de la materia: ")
    datos["Alumno"] = nombre #* SI NO EXISTE, LA LLAVE SE CREA
    datos.update({"Materia":materia}) #*  SI NO EXISTE, LA LLAVE SE CREA
    return datos

cant_alumnos = int(input("Ingrese la cantidad de alumnos a cargar: ")) #!verificar el pedido de los INPUT!!!
for i in range(cant_alumnos):
    alumno = registro()
    lista.append(alumno)
    
print("Lista de alumnos: ",lista)