from classCajero import User

#def crearUser():
#    nombre = input("Ingrese el nombre de usuario: ")
#    while True:
#        password = int(input("Ingrese la contraseña: "))
#        repeat_password = int(input('Vuelva a escribir la contraseña: '))
#        if password != repeat_password:
#            print('Se ingresaron 2 claves distintas. Verifique por favor')
#            continue
#        break
#    opcion = input('Desea ingresar un saldo inicial? S/N: ')
#    if opcion == 'S':
#        saldo=int(input('Ingrese el saldo inicial'))
#        user = User(nombre,password,saldo)
#        return user
#    user = User(nombre,password)
#    return user

def progPpal():
    user = crearUser()
    user.validarUser()
    while True:
        print()
        opcion = int(input("Elija la opcion a ejecutar:\n1)Extraccion\n2)Deposito\n3)Consulta\n4)Salir\n>>>"))
        if opcion == 1:
            monto = int(input("Ingrese un monto a extraer: "))
            user.setExtraccion(monto)
        elif opcion == 2:
            monto = int(input("Ingrese un monto a depositar: "))
            user.setSaldo(monto)
        elif opcion == 3:
            user.getSaldo()
        elif opcion == 4:
            print("Gracias por utilizar nuestro servicios.")
            break
progPpal()
