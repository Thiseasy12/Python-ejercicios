"""Dibuja un ordinograma de un programa que lea dos números y lo visualiza en orden
ascendente"""

print("Introduce el primer número:")
num1 = float(input())
print("Introduce el segundo número:")
num2 = float(input())
if num1 < num2:
    print("Los números en orden ascendente son:", num1, ",", num2)
else:
    print("Los números en orden ascendente son:", num2, ",", num1)