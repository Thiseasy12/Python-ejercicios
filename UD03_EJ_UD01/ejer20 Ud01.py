"""Dibuja un ordinograma de un programa que lea un número positivo N y calcule y visualice
su factura N! siendo el factorial:
0!=1
1!=1
2!=2*1
…
N!= N*(N-1)*(N-2)*…*1"""

print("Introduce un número positivo N:")
N = int(input())
factorial = 1
for i in range(1, N + 1):
    factorial = factorial * i
print("El factorial de", N, "es:", factorial)
