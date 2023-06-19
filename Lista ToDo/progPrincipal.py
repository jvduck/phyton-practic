import crearTodo as ct
import actualizarTodo as at
import verTodo as vt
import eliminarTodo as et

def programa():
    listado_todo=[]

    print("Bienvenidos a nuestro programa: ")

    while True:
        print()
        opciones = int(input("Elija una opcion:\n1)Crear toDo\n2)Actualizar toDo\n3)Ver listado de toDo\n4)Eliminar un toDo\n5)Salir\n>>>"))
        if opciones == 1:
            tarea = input("Ingrese la tarea a realizar: ")
            todo_creado = ct.crearTodo(tarea)
            listado_todo.append(todo_creado)
            print("Tarea agregada con exito")
        elif opciones == 2:
            vt.verTodo(listado_todo)
            completar = int(input("Elija la tarea a completar: "))
            at.actualizarTodo(listado_todo[completar-1])
        elif opciones == 3:
            vt.verTodo(listado_todo)
        elif opciones == 4:
            elemento_devuelto = et.eliminarTodo(listado_todo)
            print(f"Se elimino la tarea {elemento_devuelto.get('Tarea')}.") #Se elimino la tarea comprar alimento para el perro
        elif opciones ==5:
            print("Gracias por usar el programa.")
            break