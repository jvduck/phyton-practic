""""
TODO: vamos a crear un programa que simule el uso de un cajero. Consignas a cumplir:
-Se debe validar una clave del usuario. si es incorrecta, le decimos por favor, vuelva a ingresar la clave. Hasta que no al ingrese de manera correcta, el programa se seguira ejecutando
*El cajero tendra un menu con 4 opciones: 1)Retiro 2)Deposito 3)Consulta Saldo 4)Salir
*1) nos va a permitir retirar Saldo de nuestra cuenta
*2) nos va a permitir depositar Saldo en nuestra cuenta
*3) Nos traera el disponible que tenemos para retirar (Saldo en cuenta)
*4) Salir: finaliza el programa
-Ejecutarse mientras que la opcion no sea la de salir (podemos usar opcion de salir, o utilizar un "break" para finalizar el programa)
-El saldo, debe ser un tipo de variable, el cual nos permita Depositar o retirar, este debe ser posible de que vaya cambiando segun la operacion
"""

#? ¿Como planteamos una resolucion a un problema que requiere un algoritmo para su resolucion?
#*simulo una clave de usuario , que estaria relacionada a la tarjeta / usuario home banking
clave_usuario = 5896

clave = int(input("Ingrese su clave PIN: \n>")) #* pedir la clave pin para el ingreso al cajero

while clave_usuario != clave:
    print("Clave PIN es incorrecta")
    clave = int(input("Vuelva a ingresar la clave: "))
    
#-----------------------------------------------------------------------------#
#* simulacion del cajero operando
operacion = None #* la asignamos VACIA PARA QUE ENTRE A NUESTRO BUCLE SI O SI
saldo = 5000

while operacion != 4:
    operacion = int(input("¿Que operacion desea realizar?\n1)Retiro\n2)Deposito\n3)Consulta de saldo\n4)Salir\n>"))
    if operacion == 1:
        monto_retiro = int(input("Indique el monto a retirar:\n>"))
        if monto_retiro > saldo:
            print("Saldo insuficiente para retirar. Usted dispone de",saldo)
        else:
            saldo -= monto_retiro
            print(f"Usted retiro {monto_retiro}. Su saldo actual es de {saldo}")
    elif operacion == 2:
        monto_deposito = int(input("Ingrese el monto a depositar:\n>"))
        saldo += monto_deposito
        print(f"Su nuevo saldo es de {saldo}")
    elif operacion == 3:
        print(f"Su saldo actual es de {saldo}")
    elif operacion == 4:
        break #* este break es para ROMPER el bucle , y llevarnos al mensaje de finalizacion del sistema
    else:
        print("Opcion no valida")
        
print("Gracias por usar nuestro sistema. Hasta pronto.")