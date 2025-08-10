"""
Crear un diccionario con 6 departamentos del país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.
- Comprobar que no existe este departamento borrado dentro del
diccionario.
"""

diccionario = {"dep_1": "Lima", "dep_2": "Puno", "dep_3": "Tumbes", "dep_4": "Tacna", "dep_5": "Ica", "dep_6": "Arequipa"}

del diccionario["dep_6"]
del diccionario["dep_4"]
diccionario["dep_4"] = "Piura"
print(diccionario)

