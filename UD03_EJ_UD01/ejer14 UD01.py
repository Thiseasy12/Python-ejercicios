"""Dibuja un ordinograma que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero)."""

print("Introduce el primer número:")
num1 = float(input())
print("Introduce el segundo número:")
num2 = float(input())
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
if num2 != 0:
    division = num1 / num2
    print("La división es:", division)
else:
    print("Error: División por cero no es posible.")
print("La suma es:", suma)
print("La resta es:", resta)
print("El producto es:", producto)
