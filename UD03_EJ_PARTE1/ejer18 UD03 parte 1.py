"""Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de 10 """

print("Introduce un número:")
num = int(input())
if num % 10 == 0:
    print(f"El número {num} es múltiplo de 10.")
else:
    print(f"El número {num} no es múltiplo de 10.")
    
