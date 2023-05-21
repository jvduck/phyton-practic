#* Listas: declaracion

lista_compras=["Banana","Manzana","Arroz","Azucar"]

#print(len(lista_compras))
lista_compras.index("Arroz") #indica el numero de indice un  elemento : devolucion : 2
lista_compras.count("Manzana") #inica la cant de veces que se repite un elemento . devolucion: 1
#*-------------------------------------------------------------------------------------------*#

#? Tambien existen tuplas ANIDADAS:

#indice primario       0           1                 2                  3
#sub-indices         0    1     0     1      0          1           0     1
lista_compras_2=[["yerba",1],["Arroz",1],["Manzana","1/2 kilo"],["Pera","1 kg"]]
lista_compras_2[2][0] #* Devolucion por consola: Manzana

#* Metodos que podemos aplicar en una lista:
""""
lista_compras=["Banana","Manzana","Arroz","Azucar"]

#Agregar elementos a una lista:

lista_compras.append("Yerba") #se agrega un elemento al final de la lista
print(lista_compras)

lista_compras.insert(2,"Harina") #se agrega a un indice indicado, un elemento.
#! Si indicamos un indice que ya se encuentra ocupado, desplazara el elemento dentro de ese indice a la derecha, y luego insertara el nuevo elemento
print(lista_compras)
print(lista_compras.index("Harina"))

#actualizar un elemento de la lista:

lista_compras[4] = "Papel higienico" #indicando el indice ,podemos sustituir un elemento en una lista
print(lista_compras)

#borrar elementos de una lista:
lista_compras.pop() #elimina un elemento a traves de un INDICE. #*Si no indicamos ningun INDICE, borra el ultimo de la lista
print(lista_compras)

lista_compras.remove("Harina") #recibe un valor de un elemento a ELIMINAR
print(lista_compras)

lista_compras.clear() #vacia una lista de compras
print(lista_compras)

print(dir(lista_compras))

lista_compras.sort() #ordeno de menor a mayor nuestra lista
print(lista_compras)

lista_compras.reverse() #revierto el orden de la lista
print(lista_compras)


numeros_a=[1,2,3]
numeros_b=(4,5,6)

numeros_a.extend(numeros_b) #podemos agregar elementos de una lista a otra lista (o de una tupla a una lista)

print(dir(numeros_a))
"""

#*Iteraciones de una lista: 
#! ITERAR ES RECORRER

#? indices 0      1        2          3       4           5         6
alumnos=["Seba","Axel","Agustin","German","Valeriano","Jonatan","Facundo"]

"""
#* Primer argumento: indice de inicio. Default: 0
#* Segundo argumento: limite del recorrido de elementos. Default: final
#* Tercer argumento: saltos del recorrido de elementos. Default: 1

print(alumnos[0:7:1]) # ['Seba', 'Axel', 'Agustin', 'German', 'Valeriano', 'Jonatan', 'Facundo']
print(alumnos[0:7:3]) # ['Seba', 'German', 'Facundo']
"""

#? Otras iteraciones que tenemos en listas 

"""
#* Primer argumento negativo: toma los elementos desde el final a la "-n" indicada
#* Segundo argumento negativo: quita todos los elementos desde el final a la "-n" indicada
#* Tercer argumento negativo: recorrer en saltos INVERSOS
"""

print(alumnos[::-3]) # un indice negativo, hara un recorrido INVERSO para mostrarme el elemento


"""
#? Ejercitacion 1:

1) Crear una lista con 6 elementos tipo string
2) Agregan 1 elemento al final
3) Agregan un elemento al indice 4
4) Reemplazan el elemento del indice 3 por otro elemento
5) Eliminan un elemento a eleccion a traves de su indice. #!NO PUEDE SER EL ULTIMO ELEMENTO
6) Eliminan un elemento a traves de su dato 

#? Ejercitacion 2:

1) crear una lista con 5 elementos string
2) A esa lista, le agregaran otra lista con 4 elementos string, para formar una sola
3) Van a recorrer esa lista desde el indice 1 hasta el elemento 6
4) van a recorrer esa lista pero de 2 en 2
5) Van a recorrer esa lista pero de manera inversa, desde el penultimo elemento (anterior al ultimo) al tercer elemento de la lista
#? 6) EXTRA: recorrer toda la lista en reversa, pero sin usar el tercer argumento en negativo NI EL METODO REVERSE O SORT CON REVERSED=TRUE. (NO OBLIGATORIO)
"""

