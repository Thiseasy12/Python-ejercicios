"""Dibuja un ordinograma de un programa que lea un número y dice si es positivo o negativo,
consideramos el cero como positivo."""

print("Introduce un número:")
num = float(input())
if num >= 0:
    print("El número es positivo")
else:
    print("El número es negativo")
    