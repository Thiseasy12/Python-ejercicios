"""Dibuja un ordinograma de un programa que lee dos números y muestra el mayor."""

print("Introduce el primer número:")
num1 = float(input())
print("Introduce el segundo número:")
num2 = float(input())
if num1 > num2:
    print("El mayor es:", num1)
else:
    print("El mayor es:", num2)
    