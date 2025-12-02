"""Dibuja un ordinograma de un programa donde el usuario “piensa” un número del 1 al 100
y el ordenador intenta adivinarlo. Es decir, el ordenador irá proponiendo números una y otra
vez hasta adivinarlo (El usuario deberá indicarlo al ordenador si es mayor o menor o igual al
número pensado)"""

print("Piensa un número del 1 al 100 y yo intentaré adivinarlo.")
bajo = 1
alto = 100
intento = (bajo + alto) // 2
while True:
    print("¿Es tu número", intento, "?")
    respuesta = input("Introduce 'mayor', 'menor' o 'igual': ").lower()
    if respuesta == 'igual':
        print("¡He adivinado tu número", intento, "!")
        break
    elif respuesta == 'mayor':
        bajo = intento + 1
    elif respuesta == 'menor':
        alto = intento - 1
    else:
        print("Respuesta no válida. Por favor, introduce 'mayor', 'menor' o 'igual'.")
        continue
    intento = (bajo + alto) // 2
    if bajo > alto:
        print("Parece que ha habido un error. ¿Estás seguro de tus respuestas?")
        break
    
print("Gracias por jugar.")

