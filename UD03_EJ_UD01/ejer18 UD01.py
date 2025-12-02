"""Dibuja un ordinograma de un programa que lea dos números y nos diga cual es mayor o si
son iguales."""

print("Introduce el primer número:")
num1 = float(input())
print("Introduce el segundo número:")
num2 = float(input())
if num1 > num2:
    print("El mayor es:", num1)
elif num2 > num1:
    print("El mayor es:", num2)
else:
    print("Los números son iguales.")