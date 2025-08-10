"""
Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u
"""

diccionario = {"nombre": "Rodrigo", "edad": 25, "salario": 1500}

diccionario["carrera"] = "Biología"
var_1 = diccionario["carrera"]
var_2 = diccionario["nombre"]

print("La carrera de {} es {}.".format(var_2, var_1))
