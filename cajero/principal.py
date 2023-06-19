
from validar import validar
from consultar import consulta
from extraer import extraccion
from depositar import deposito

"""
El programa tiene 4 opciones: extraccion, deposito, consulta, salir.
Antes de ejecutar el programa principal, debemos validar que el usuario ingrese la contraseña correcta.
#? VALIDADORES TRUE PARA SENTENCIAS 
validador = True # PUEDE TMB VALER FALSE
#al momento de darle un valor a mi validador NO NECESITO COMPARARLO CON OTRA VARIABLE, YA QUE CONTIENE UN VALOR DEL TIPO BOOLEANO
if validador:
    print("El validador es verdadero")
    
SENTENCIAS NO VALIDAS: dan como resultado un False
ej: string vacios (""), numero 0 (dato Integer), booleano False , dato tipo nulo: None
"""


def progPpal():
    validar()
    saldo = 15000

    while True:
        print()
        opcion = int(input("Elija la opcion a ejecutar:\n1)Extraccion\n2)Deposito\n3)Consulta\n4)Salir\n>>>"))
        if opcion == 1:
            monto = int(input("Ingrese un monto a extraer: "))
            saldo = extraccion(monto,saldo)
        elif opcion == 2:
            monto = int(input("Ingrese un monto a depositar: "))
            saldo = deposito(monto,saldo)
        elif opcion == 3:
            consulta(saldo)
        elif opcion == 4:
            print("Gracias por utilizar nuestro servicios.")
            break
