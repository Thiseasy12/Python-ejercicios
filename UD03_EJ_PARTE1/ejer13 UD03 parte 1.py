"""Escriba un programa que lea dos números y lo visualiza en orden ascendente"""
print("Dame un numero")
num1 = int(input())
print("Dame otro numero")
num2 = int(input())
if num1 < num2:
    print("Los numeros en orden ascendente son:", num1, ",", num2)
else:
    print("Los numeros en orden ascendente son:", num2, ",", num1)