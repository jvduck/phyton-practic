#FUNCIONES

#? ¿Que es una funcion?. Es un fragmento de codigo que se ejecuta al momento que lo INVOCAMOS/LLAMAMOS. La funcion nos permite que sea llamada varias veces dentro de nuestro codigo, y de esta manera evitar tener que repetir piezas de codigo innecesarias (DRY).

#* declaracion de la funcion
def saludo():
    print("Hola! Bienvenido a Python")


saludo() #* de este modo, la invocamos

#*funcion con argumento

def bienvenida(nombre,apellido):
    print(f"Hola {nombre} {apellido} bienvenido a Python")


bienvenida("Julian","perez")
bienvenida("Axel","gomez")
bienvenida("Seba","diaz")

usuario="Facu"
bienvenida(usuario,"marcos") #! no importa si pasamos un dato, una variable u otro, siempre y cuando respete la posicion del argumento

#* argumentos declarados: estos argumentos YA LLEVAN UN VALOR DENTRO DEL PARAMETRO DE LA FUNCION

#*una funcion que me devuelve un numero al cuadrado

def cuadrado(numero, x=2 ):
    print(f"el numero {numero} al cuadrado es {numero**x}")

cuadrado(8)

"""
TODO: crear una funcion que reciba 2 argumentos: un numero y luego otro (estos son pedidos a traves de 2 input distintos, al usuario). Esta funcion tomara esos 2 numeros los multiplicara y devolvera el resultado. Ej: si recibo 4 y 7, La multiplicacion de 4 y 7 es 28.
"""

def multiplicacion(num1,num2):
    resultado = num1 * num2
    print(f'El resultado de la multiplicacion entre {num1} y {num2} es: {resultado}')
    

numero1=int(input("Por favor, ingrese el primer numero:\n>>>"))
numero2=int(input("Por favor, ingrese el segundo numero:\n>>>"))

multiplicacion(numero1,numero2)