#? RESTANTES DE BUCLE WHILE
"""
while True:
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))
    if num2 == 0:
        print("ERROR: el segundo numero es cero. Es imposible dividir en base 0")
        continue #! VOLVIA AL PRINCIPIO DEL BUCLE
    result = num1/num2
    print("El resultado es",result)
    break #!ROMPIA EL BUCLE



#? COUNTER:  los contadores nos sirven para poder ejecutar un while , hasta que la condicion se cumpla, PERO de una manera ACUMULATIVA

#* Vamos a pedirle a las 5 personas que estan en la mesa, que nos digan que cerveza quiere tomar

pedido_cervezas = 0
rubias = 0
rojas = 0
ipa = 0

while pedido_cervezas < 7:
    cerveza = input("Que cerveza desea pedir? :")
    pedido_cervezas += 1 #! es lo mismo que decir => pedido_cervezas = pedido_cervezas + 1
    if cerveza == 'rubia':
        rubias += 1
    elif cerveza == 'roja':
        rojas += 1
    elif cerveza == 'ipa':
        ipa += 1

print(f" Se pidieron {rubias} rubias, {rojas} rojas y {ipa} ipas")
"""

#! DESESTRUCTURACION DE ITERABLE
lista = ["Juan","Seba","Lucas"]

alumno1, alumno2,alumno3 = lista


#? BUCLE FOR
"""
lista_compras = ["Banana","Manzana","Pera","Uva","Naranja"]

for i in lista_compras:
    print(i)
"""

"""
print(formulario.items())
#* Metodo 1: para imprimir llaves y valro en un recorrido en un diccionario
for dato in formulario:
    print("LLave:" ,dato)
    print("Valor:" ,formulario.get(dato)) #* nos devuelve el valor de una llave
    
#*Metodo 2: 
for dato in formulario.keys(): #! EQUIVALE A RECORRER UNA LISTA QUE ALMACENA LAS LLAVES
    print(dato) #* Esto em va a imprimir cada LLAVE
    
#*Metodo 2-Bis: 
for dato in formulario.values(): #! EQUIVALE A RECORRER UNA LISTA QUE ALMACENA LOS VALORES
    print(dato) #* Esto me va a imprimir cada VALOR
    

formulario={"Nombre":"Seba","Edad":35,"Mascota":"Gamora","Ciudad":"Mar del Plata"}

#* Metodo 3:
for llave,valor in formulario.items():
    print("Llave:",llave)
    print("Valor:",valor)
"""
#TODO: EJEMPLO DE USO DE CASO DE DESESTRUCTURACION

lista_curso =[["Seba",3],["Lujan",10],["Mariano",9],["Emilse",1]]
"""
for alumno,nota in lista_curso:
    if nota < 4:
        print(f"El alumno {alumno} no aprobo")
    else:
        print(f"El alumno {alumno} esta aprobado")
"""       
try:
    resultado = 2/0
except Va
    print("Error")