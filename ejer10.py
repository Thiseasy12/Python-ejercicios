"""Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero)."""

print("Dame un numero")
num1 = int(input())
print("Dame otro numero")
num2 = int(input())
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
if num2 != 0:
    division = num1 / num2
    print("La división es", division)