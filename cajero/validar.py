contrasenia = [1596,2589,1697,2582]

# a traves de un FOR - IN podria verificar si se encuentra o no, la pass en el listado

#variable para VALIDAR la clave
def validar():
    while True:
        validador = True
        usuario = int(input("Ingrese su clave de Seguridad: "))
        for clave in contrasenia:
            if usuario == clave:
                print("Bienvenido nuevamente.")
                validador = False
        if validador:
            print("Clave invalida. Intente Nuevamente.")
        else:
            break