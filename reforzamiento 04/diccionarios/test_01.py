"""
Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal.
"""

diccionario = {"nombre": "Camilo", "edad": 25, "salario": 1500}

lista_claves = list(diccionario.keys())
lista_valores = list(diccionario.values())
lista_items = list(diccionario.items())

print("La lista de claves es: {}".format(lista_claves))
print("La lista de valores es: {}".format(lista_valores))
print("La lista de items es: {}".format(lista_items))
