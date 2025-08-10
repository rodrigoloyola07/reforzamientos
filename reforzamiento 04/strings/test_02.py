"""
Crear un programa que cuente cuántas veces aparece cada vocal en la
oración. Ignorar mayúsculas/minúsculas
Input: “Programación en Python”
Output:
a: 2
e: 1
i: 1
o: 2
u: 0
Métodos útiles: lower() y count()
"""

frase = "Programación en Python"
frase.lower()
a = frase.count("a")
e = frase.count("e")
i = frase.count("i")
o = frase.count("o")
u = frase.count("u")

print("\na: {}\ne: {}\ni: {}\no: {}\nu: {}".format(a, e, i , o, u))