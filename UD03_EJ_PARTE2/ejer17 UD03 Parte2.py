"""Programa que suma independientemente los pares y los impares de los números
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas."""

suma_pares = 0
suma_impares = 0
for i in range (100,201):
    if i % 2:
        suma_impares += 1
    else:
        suma_pares +=1
print(f"La suma de los numeros pares es: {suma_pares}")
print(f"La suma de los numeros impares es: {suma_impares}")
   