"""Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola."""

lista_estudiantes = ["Rodrigo", "Pedro", "Jair", "Carlos", "Danny"]

nombre_estudiante = input("Ingrese el nombre del estudiante: ")

if nombre_estudiante in lista_estudiantes:
    lista_estudiantes.remove(nombre_estudiante)
else:
    print("El estudiante no se encuentra en la lista")
    lista_estudiantes.append(nombre_estudiante)
print("La lista actualizada es: {}".format(lista_estudiantes))
