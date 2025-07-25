"""Crea un programa que calcule el Índice de Masa Corporal (IMC) de
una persona.
La fórmula es: IMC = peso (kg) / altura (m)2

En el mensaje también indicar el nombre de la persona indicando su
IMC también"""

# Creación de variables
nombre = "Rodrigo"
apellido = "Loyola"
peso = 60.4    # en kg
altura = 1.68  # en m

# Fórmula de IMC
imc = peso / pow(altura, 2)

# Mensaje
print('Señor(a) {} {}, su IMC es {}'.format(nombre, apellido, f'{imc:.1f}'))
