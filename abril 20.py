#Diccionarios

#* Los diccionarios ,a  diferencia de una lista, no poseen INDICES, sino que son pares ordenados por llave:valor

# metodo: 'clear', 'copy', 'fromkeys',  'pop', 'popitem', | 'values','get', 'items', 'keys','setdefault', 'update' 
agenda={
    "nombre":"Seba",
    "edad":35,
    "ciudad":"mar del plata"
    }

#? Metodos de Diccionarios

#* Leer elementos
"""
print(agenda.keys()) #* Nos devuelve UNA LISTA DE LAS LLAVES
print(agenda.values()) #* Nos devuelve UNA LISTA DE LOS VALORES
print(agenda.items()) #* Nos devuelve una lista con tuplas anidadas, en el cual cada tupla contiene LLAVE/VALOR
print(agenda.get("nombre")) #* Nos devuelve EL VALOR  de UNA LLAVE
print(agenda["nombre"]) #* podemos usa bracket notation para que nos devuelva EL VALOR DE UNA LLAVE
"""
#? agregar items

agenda.setdefault("mascota") #* creamos una nueva llave 
agenda.setdefault("profesion","programador y profesor") #* de manera opcional PODEMOS DARLE UN VALOR INICIAL
print(agenda)

#? actualizar item
agenda.update({"edad":21}) #! IMPORTANTE: PASAR LOS ARGUMENTOS COMO UN DICCIONARIO: LLAVE:VALOR
agenda["ciudad"] = "Paris" #* mediante BRACKET NOTATION, tambien podriamos cambiar el valor
agenda.update({"estado civil":"soltero"})

print(agenda)

#? eliminar items

agenda.pop("mascota") #* vacia segun la llave asignada
agenda.popitem() #! IMPORTANTE: POPITEM ELIMINA LA ULTIMA LLAVE CREADA. NO UTILIZAR SI VAN A ELIMINAR DESDE LOS VALORES DE LLAVE
print(agenda)
agenda.clear() #* vacia el diccionario

#? crea un diccionario a traves de una lista en el cual cada valor es una llave

#lista=["nombre","apellido","dni"]
lista={"Nombre":"seba","Apellido":"asd","dni":1111111}
valor = "aca va un valor"
datos=dict.fromkeys(lista)
print(datos)
