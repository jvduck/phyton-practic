def crearLista(num):
    lista = []
    for i in range(num):
        articulo = input("ingrese articulo: ")
        cantidad = int(input("ingrese cantidad: "))
        orden = [articulo,cantidad]
        lista.append(orden)
    return lista
def mostrarLista(lista):
    for i in lista:
        print("elementos a comprar: ",i)
        
    
    