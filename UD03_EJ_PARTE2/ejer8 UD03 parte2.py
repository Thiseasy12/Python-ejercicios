"""Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos son positivos y cuantos negativos."""

contador_posiitivos = 0
contador_negativos = 0
for i in range(100):
    numero = int(input("Introduce un numero no nulo:"))
    if numero > 0: 
        contador_negativos *= 1
    else:
        contador_posiitivos *= 1
    