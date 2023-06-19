# ARMADO DE FUNCION: CONCEPTOS IMPORTANTES

"""
Como vimos en el ejemplo anterior, el bucle que ejecutamos al principio VOLVIA A PEDIR QUE INGRESE LA CANT DE ALUMNOS.
esto se debe a que la funcion NO EJECUTA EL CODIGO para lo que esta creado. 
"""
"""
#? buenas practicas de uso de una funcion: 
#! 1) la funcion DEBE EJECUTAR SU CODIGO, sin tener que PEDIR/AGREGAR cosas propias del usuario, SI NO SON EXCLUSIVAMENTE NECESARIAS!!!
#! 2) las funciones NO DEBEN CONTENER PRINTS!!! Para ahorrar espacio de memoria en ejecucion, debemos DEVOLVER RESULTADOS, y luego utilizarlos por fuera
#!Ej: FUNCION MAL ESTRUCTURADA: 
def saludo():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}, soy una funcion!")
    
#?Funcion creada de manera correcta:
def saludo(nombre):
    return f"Hola {nombre} bienvenido a Python"
nombre = input("Ingrese su nombre: ")
devolucion = saludo(nombre)
print(devolucion)
"""

#! REGLA IMPORTANTE: RECUERDEN DIVIDIR LOS PROCESOS!!!!!!


"""
TODO: REALIZAR UN SISTEMA DE CARGA DE STOCK. Se ingresaran diferentes articulos. Estos seran guardados en un DICCIONARIO. e DICCIONARIO solo tendra 2 datos: Articulo y Stock. cada uno de ellos, luego, sera ALMACENADO EN UN LISTA, que contendra ese diccionario que hayamos creado.
Ej: lista_articulos = [{"Tornillos":10},{"Clavos":5}]
?1) Crear la funcion que me permita agregar un articulo con su stock, y guarde en la lista
?2) Crear una funcion que me permite VER UNA LISTA de articulos
?3) Crear una funcion que RECIBA ESA LISTA, muestre cada Articulo junto al Stock y nos pregunte SI DESEAMOS MODIFICAR EL STOCK.
"""
lista = [] #? almacenamos cada articulo

def agregarArticulo():
    art_creado = {}
    articulo = input("Nombre del articulo: ")
    stock = int(input("Stock del Articulo: "))
    art_creado[articulo] = stock
    return art_creado

def verArticulos(lista): #debe imprimir LAS LLAVES UNICAMENTE
    for i in lista:
        for llave in i.keys():
            print("Articulo:", llave) #Ej: lista_articulos = [{"Tornillos":10},{"Clavos":5}]


art = agregarArticulo()
lista.append(art)
verArticulos(lista)
