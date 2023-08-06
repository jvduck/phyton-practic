#verTodo: recorre una lista y me muestra cada elemento que hay dentro

def verTodo(listado: list):
    for i in listado:
        if i["Estado"] == True:
            estado = "completo"
        else:
            estado = "pendiente"
        print(f'Tarea: {i["Tarea"]}, Estado: {estado}')

listado = (sarasas)        
verTodo()