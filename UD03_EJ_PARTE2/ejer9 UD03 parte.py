"""Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos"""

hay_negativo = False
contador_positivos = 0
contador_negativos = 0
while True:
    numero = int(input("Introduce un numero no nulo(con 0 se acaba el programa):"))
    if numero == 0:
        break
    if numero <0: 
        hay_negativo = True
        contador_negativos+=1
    else:
        contador_positivos+=1
if hay_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")
print(f"Cantidad de números positivos: {contador_positivos}")
print(f"Cantidad de números negativos: {contador_negativos}")