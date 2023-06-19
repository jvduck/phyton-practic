#¿Como importamos un archivo o como importamos una funcion?

#? para importar un archivo COMPLETO:
"""
import principal as pp #le doy un alias, para poder utilizarlo en mi codigo:
#from principal import funcion_que_no_existe

cantidad = int(input("Indique cuantos articulos va a comprar: "))
lista = pp.crearLista(cantidad)
print(lista)
"""
#? importar una unica FUNCION a mi archivo

from principal import mostrarLista

lista1 = [['Harina', 2], ['Yerba', 1], ['Arroz', 2]]
mostrarLista(lista1)