"""Escribe un programa que reciba dos flotantes, luego estos pasarán a
ser convertidos en enteros. Indique si el primero es múltiplo del
segundo. Usar mod para la verificación si el residuo es 0"""

# Creación de variables
float_1 = 45.28
float_2 = 6.325

# Conversión de float a int
int_1 = int(float_1)
int_2 = int(float_2)

# Verificando si int_1 es múltiplo de int_2
if int_1 % int_2 == 0:
    print('{} es múltiplo de {}'.format(int_1, int_2))
if int_1 % int_2 > 0:
    print('{} NO es múltiplo de {}'.format(int_1, int_2))
