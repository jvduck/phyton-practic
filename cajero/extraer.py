def extraccion(monto,saldo):
    while True:
        if monto > saldo:
            print(f"Fondo insuficiente, su saldo es de {saldo}. Ingrese otro importe")
            monto = int(input("Ingrese un monto a extraer: "))
            continue
        resto = saldo - monto
        print(f"Se ha retirado {monto} de su cuenta ")
        return resto