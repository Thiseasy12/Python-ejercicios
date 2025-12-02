"""Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales 
son iguales"""

print("Dame un número")
num1 = int(input())
print("Dame otro número")
num2 = int(input()) 
print("Dame un tercer número")
num3 = int(input())
if num1 == num2 and num1 == num3:
    print("Los tres números son iguales")
elif num1 >= num2 and num1 >= num3:
    print("El número mayor es:", num1)
    if num2 <= num3:
        print("El número menor es:", num2)
    else:
        print("El número menor es:", num3)