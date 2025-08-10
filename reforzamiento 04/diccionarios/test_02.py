"""
Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado.
"""

diccionario = {"nombre": "Camilo", "edad": 25, "salario": 1500}

diccionario["dni"] = 44680324
print("El valor del salario es: {} y el valor del DNI es: {}".format(diccionario["salario"], diccionario["dni"]))

del diccionario["edad"]
print("El diccionario actualizado es: {}".format(diccionario))