"""
Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tienes.
"""

diccionario = {"nombre": "Camilo", "edad": 25, "salario": 1500}

lista_claves = list(diccionario.keys())
lista_valores = list(diccionario.values())
lista_items = list(diccionario.items())

print("El tipo de datos de la lista es: {}".format(type(lista_claves)))
print("El tipo de datos de la lista es: {}".format(type(lista_valores)))
print("El tipo de datos de la lista es: {}".format(type(lista_items)))