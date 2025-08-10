"""
Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario.
"""

diccionario = {}

for número in range(4):
    numero = int(input("Ingrese número: "))
    diccionario[numero] = pow(numero, 3)

print("El diccionario creado es: {}".format(diccionario))
