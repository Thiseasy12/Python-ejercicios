"""Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla."""

A = int(input("Introduce el valor de A: "))
B = int(input("Introduce el valor de B: "))
resultado = 1
for _ in range(B):
    resultado *= A
print(f"El resultado de {A}^{B} es: {resultado}")
