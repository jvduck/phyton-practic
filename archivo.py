nombre = input("Digame su nombre: ")

""" #opcion 1 : concatenar
print("Hola "+nombre)

#opcion 2: separador por comas
print ("Hola",nombre)

#opcion 3: metodo f-string
print(f"Hola {nombre}")
"""

anio_nacimiento = input("ingrese su año de nacimiento: ")
#la variable de nacimiento es de tipo string, por om tanto debemos convertirla a integer
edad=2023-int(anio_nacimiento)

#opcion 1: concatenar
print("Hola "+nombre+" tu edad es de "+str(edad))

#opcion 2: separar por coma
print("Hola",nombre,"tuedad es de ",edad)

#opcion 3: metodo f-string
print(f"Hola {nombre} tu edad es de {edad}")