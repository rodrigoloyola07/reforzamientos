"""Escribe un programa que convierta cierta cantidad de soles a dólares,
usando un tipo de cambio que se proporciona en el programa.
Estos valores estarán dentro de sus variables respectivamente.
La salida mostrará tres cambios que hagas respectivamente de tres
montos a convertir."""

# Tipo de cambio (factor de conversión)
pen_usd = 0.28 # 1 PEN = 0.28 USD

# Creación de variables
monto_pen_1 = 948
monto_pen_2 = 2300.50
monto_pen_3 = 4680

# Conversión utilizando dos decimales
monto_usd_1 = pen_usd * monto_pen_1
monto_usd_2 = pen_usd * monto_pen_2
monto_usd_3 = pen_usd * monto_pen_3
print('{} PEN son {} USD'.format(monto_pen_1, f'{monto_usd_1:.2f}'))
print('{} PEN son {} USD'.format(monto_pen_2, f'{monto_usd_2:.2f}'))
print('{} PEN son {} USD'.format(monto_pen_3, f'{monto_usd_3:.2f}'))
