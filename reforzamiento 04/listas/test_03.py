"""Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado
insertados en la terminal"""

lista = []

lista.append(10)
lista.append(20)
lista.append(30)
lista.append(40)
lista.append(50)
lista.append(60)
lista.append(70)
lista.append(80)
lista.append(90)
lista.append(100)
print("La lista de número es: {}".format(lista))

suma = sum(lista)
print("La suma de los valores de mi lista es: {}".format(suma))
print("La media de los valores de mi lista es: {}".format(f'{suma/len(lista):.0f}'))
