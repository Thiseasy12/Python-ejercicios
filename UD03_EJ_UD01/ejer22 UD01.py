"""Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un
mensaje indicando cuántos son positivos y cuantos negativos."""

contador_positivos = 0
contador_negativos = 0
for _ in range(100):
    print("Introduce un número no nulo:")
    numero = float(input())
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1