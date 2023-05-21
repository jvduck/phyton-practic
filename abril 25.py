#condicionales

#* IF-ELIF-ELSE:

"""
interruptor = "On" #* contiene el estado del interruptor: ON u OFF
corriente = True #* si la corriente es True , la lamparita podra encenderse
tension = 220

#*operadores logicos > , < , >= ,<= , == ,!=
#* conectores logicos and, or , not  ( && , || , !)

if interruptor == "On" and corriente == True and tension == 220:
    print("La lamparita esta prendida.")
elif interruptor == "Off" or corriente == False or tension != 220:
    print("La lamparita esta apagada.")
else:
    print("Ha ocurrido un error al chequear la lamparita.")

!JERARQUIAS: Al igual que en matematica, Python resuelve parentesis (si tuvieses), y luego ejecuta de izquierda a derecha
variable_1 = 10
variable_2 = 20
variable_3 = 35

if variable_1 > 10 and (variable_2 > 20 or variable_3 > 30):
    print("Se ejecuta.")
"""

#? MATCH: ejecuta un bloque dependiendo el parametro a evaluar:

#* Tenemos 3 deptos: con el 1 llamamos a Seba, el 2 a Sandra, el 3 a Gustavo. los otros botones del portero, comunican a porteria
"""
match depto:
    case 1:
        print("LLamando a Seba")
    case 2:
        print("Llamando a Sandra")
    case 3:
        print("Llamando a Gustavo")
    case _:
        print("Llamando a porteria")
"""

#? Bucles:
#! para ejecutar un while, nuestras variables de condicion, tienen que estar declaradas antes
"""
from random import randint #* nos permite crear con el randint, un numero aleatorio

numero_secreto = randint(1,100) #* genero un numero aleatorio entre 1,100
numero_arriesgado = None

while numero_secreto != numero_arriesgado:
    numero_arriesgado = int(input("Ingrese un numero entre 1 y 100: "))
    if numero_arriesgado > numero_secreto:
        print("El numero ingresado es mas alto que el secreto!")
    elif numero_arriesgado < numero_secreto:
        print("El numero ingresado es mas bajo que el secreto!")
    else:
        print(f"Acertaste!!! El numero era {numero_secreto}")
"""
#* break nos permite terminar un bucle a la fuerza (romper la condicion)
#* continue, nos obliga a volver al principio del bucle:


"""
while True:
    input("Presione enter:")
    print("Usted presiono enter.")
    print("Esta linea esta al final")
    print("Destruyamos el bucle")
    break
"""

while True:
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))
    if num2 == 0:
        print("el segundo numero es cero")
        continue
    result = num1/num2
    print(result)