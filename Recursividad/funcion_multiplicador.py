#RECURSIVIDAD: Una funcion recursiva es una funcion la cual se llama asi misma

#crear una funcion que simule la multiplicacion: ej: si pongo en mi funcion 5 y 8, me devuelve 40

#! en una recursividad SIEMPRE EXISTE UN CASO DE CORTE
#? EN EL RETURN SE INVOCA/LLAMA A SI MISMA

"""
* 5 x 8 => 5+5+5+5+5+5+5+5
* 6 x 3 => 6+6+6
* 7 x 4 => 7+7+7+7
"""

def multiplicar(base,multiplicador):
    if multiplicador > 1:
        return base + multiplicar(base,multiplicador-1)
    return base

#  multiplicar(3,5) => 3 + multiplicar(3,4) => 
#  3 + ( 3 + multiplicar(3,3)) 
#  3 + ( 3 + ( 3 + multiplicar(3,2)))
#  3 + ( 3 + ( 3 + 3 + multiplicar(3,1)))
#  3 + ( 3 + ( 3 + 3 + (3)))

print(multiplicar(7,7))