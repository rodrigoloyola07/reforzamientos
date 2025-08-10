"""
Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de
TI) y harás una copia donde adrede agregarás nombres que estarán
repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista
inicial
"""

tamano_lista = int(input("Ingresar la cantidad de datos: "))
lista_ti = []

for tamano in range(tamano_lista):
    nombre = input("Ingresar nombre de la compañía relacionada a la TI: ")
    lista_ti.append(nombre)

lista_copy = lista_ti.copy()

cantidad_repetidos = int(input("Ingresar cantidad de compañías repetidas: "))
for tamano in range(cantidad_repetidos):
    repetido = input("Ingresar nombre repetido de la compañía: ")
    lista_copy.append(repetido)

lista_sin_repetidos = []
for nombre in lista_copy:
    lista_sin_repetidos.append(nombre)

print("La lista inicial de compañías es: {}".format(lista_ti))
print("La lista con compañías repetidas es: {}".format(lista_copy))
print("La lista sin compañías repetidas es: {}".format(lista_sin_repetidos))








