"""Dibuja un ordinograma de un programa que lea tres números y nos diga cual es mayor, cual
menor y cuales son iguales"""

print("Introduce el primer número:")
num1 = float(input())
print("Introduce el segundo número:")
num2 = float(input())
print("Introduce el tercer número:")
num3 = float(input())
if num1 >= num2 and num1 >= num3:
    mayor = num1
    if num2 >= num3:
        menor = num3
        medio = num2
    else:
        menor = num2
        medio = num3