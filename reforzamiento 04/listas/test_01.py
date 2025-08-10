"""
Escribir un programa donde ingresarás el tamaño de la lista mediante
consola, este tamaño servirá para ingresar una cantidad X de nombres de
alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de
la lista que fueron ingresados.
"""

tamano_lista = int(input("Ingresar la cantidad de alumnos: "))
alumnos_lista = []

for tamano in range(tamano_lista):
    nombre = input("Ingresar nombre de alumno: ")
    alumnos_lista.append(nombre)
print("La cantidad de alumnos es: {}".format(len(alumnos_lista)))
print("Los nombre de los alumnos son: {}".format(alumnos_lista))
