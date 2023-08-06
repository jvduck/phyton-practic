from clases import Alumnos,Profesores,Curso

#creacion de un alumno: simular el pedido de datos a un usuario, para cargar un alumno.

nombre = input('Ingrese el nombre: ')
apellido = input('Ingrese el apellido: ')
dni = input('Ingrese el DNI (sin puntos): ')
anio_cursada = input('Ingrese el anio que esta cursando: ')

alumno = Alumnos(nombre,apellido,dni,anio_cursada)

#creacion de un profesor

nombre = input('Ingrese el nombre: ')
apellido = input('Ingrese el apellido: ')
dni = input('Ingrese el DNI (sin puntos): ')
materia = input('Ingrese la materia que dicta: ')

# profesor = Profesores(nombre,apellido,dni,materia)

#creacion de un curso:

curso = Curso()

profesor = Profesores('Seba','Perez','33456789','Programacion')

alumno1 = Alumnos('Pedro','Gomez','34345678','2do')
alumno2 = Alumnos('Laura','Vazquez','45345434','2do')
alumno3 = Alumnos('Lionel','Messi','33123432','2do')

curso.setCurso('Programacion')
curso.setProfesor(profesor) #como argumento, le pasaremos el profesor creado en la clase Profesores
curso.setAlumnos(alumno1)
curso.setAlumnos(alumno2)
curso.setAlumnos(alumno3)

print(curso)

curso.getAlumnos()