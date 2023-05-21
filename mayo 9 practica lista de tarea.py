
lista_todo = []
print(len(lista_todo))
while True:
    opcion = int(input("Elija una opción: \n1)Listar TODOs\n2)Agregar nuevos\n3)Eliminar una lista\n4)Salir\n"))
    if opcion == 1:
        if len(lista_todo) == 0:
            print("lista vacia. ")
        else:
            for i in range(len(lista_todo)):
                print(f"{i+1}->> {lista_todo[i]}")
    elif opcion == 2:
        while True:
            tarea = input("ingrese la tarea a realizar: ")
            lista_todo.append(tarea)
            print(f"{tarea} fue agregada a la lista")
            repetir = input("¿Desea agregar otr tarea? S/N: ")
            if repetir == "N" or repetir == "n":
                break
    elif opcion == 3:
        while True:
            if len(lista_todo) == 0:
                print("No hay tarea para eliminar.")
                break
            else:
                for i in range(len(lista_todo)):
                    print(f"{i+1}- {lista_todo[i]}")
                eliminar = int(input("Elija la tarea a eliminar: "))
                tarea_eliminada = lista_todo.pop(eliminar-1)
                print(f"{tarea_eliminada} fue eliminada de la lista.")
                break
    elif opcion == 4:
        print("gracias por usar nuestro programa")
        break
    else:
        print("entrada invalidad; por favor elija otra opcion")