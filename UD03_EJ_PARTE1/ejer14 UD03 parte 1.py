"""Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales."""
print("Dame un número")
num1 = int(input())
print("Dame otro número")
num2 = int(input())
if num1 > num2:
    print("El numero mayor es:",num1)
elif num2 > num1:
    print("El numero mayor es:",num2)
else:
    print("Los numeros son iguales")