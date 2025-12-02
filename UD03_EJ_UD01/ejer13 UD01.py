"""Dibuja un ordinograma de un programa que muestre los números desde el 1 hasta el
número N que se introducirá por teclado."""

print("Introduce los numeros")
N = int(input())
for numero in range(1, N + 1):
    print(numero)
    