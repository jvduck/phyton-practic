#crea un diccionario en el cual el string pasado sera el valor de la llave tarea y tiene como "estado" False esto significa que la tarea 
# todavia no se realizo

def crearTodo(string: str):
    toDo={"Tarea":None,"Estado":False}
    toDo["Tarea"] = string
    return toDo
