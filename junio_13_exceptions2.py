"""
! NameError: intento llamar a una variable que NO EXISTE
! IndexError :el emento al cual se intenta acceder esta fuera de rango
! SyntaxError: hay un error en la sintaxis de lo escrito en el codigo!
! KeyError: intentamos acceder a llave inexistente!
! TypeError: Invalida comparaciones u operaciones entre distintos tipos de dato
! ValueError: estoy intentano utilizar una funcion/metodo sobre un valor el cual es imposible convertir
! ImportError /ModuleNotFound: Estamos intentando importar un modulo inexistente o una funcion inexistente
! ZeroDivisionError: Dividir por 0

"""

#? clausulas try-except-else-finally

# try:
#     division = 15/5
#     resta = int("4")-int("t")
#     suma = int("6")+int("8")
# except Exception as er:
#     error = er
# else: #el else FUNCIONA EN BASE A LA EXCEPCION: si el Except se ejecuta, el ELSE no lo hara
#     print("El resultado de la division es:",division)
#     print("El resultado de la suma es",suma)
#     print("El resultado de la resta es",resta)
# finally: #no importa que ocurra, se ejecuta
#     print("Aca se ejecuto mi finally")
    
# if error:
#     print("Hay un error en los datos ingresados")
    
# print(type(error)) #como podemos ver, es un OBJETO! por lo tanto , existe!!


##? EJEMPLO PRACTICO: validemos que el usuario ingrese de manera correcta los datos!


def formulario(nombre,ciudad,edad,peso):
    if not nombre or not ciudad:
        print("Por favor ingrese sus datos de nombre o ciudad!")
        return 
    try:
        edad = int(edad)
        peso = float(peso)
    except Exception as error:
        print("Ingrese nuevamente los datos NUMERICOS pedidos")
        return
    else:
        print("Gracias por ingresar sus datos")

while True:
    nombre= input("Ingrese su nombre: ")
    ciudad= input("Ingrese su ciudad: ")
    edad= input("Ingrese su edad: ")
    peso= input("ingrese su peso: ")
    datos = formulario(nombre,ciudad,edad,peso)
    if not datos: #el None entra dentro del grupo de "Falsies" cuando los validamos de manera aislada
        print("Hubo error en datos")
        continue
    break