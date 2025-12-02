"""Programa donde el usuario "piensa" un número del 1 al 100 y el ordenador intenta
adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el
usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado)."""

print("Piensa un numero entre el 1 y el 100")
minimo = 1
maximo = 100
intentos = 0
while True:
    intentos += 1
    adivinanza = (minimo + maximo) // 2
    respuesta = input(f"¿Es {adivinanza} tu número? (mayor/menor/igual): ").lower()
    if respuesta == "igual":
        print("He adivinado el numero",adivinanza,"en",intentos,"intentos")
        break
    elif respuesta == "mayor":
        minimo = adivinanza + 1
    elif respuesta == "menor":
        maximo = adivinanza - 1
    else:
        print("Respuesta no válida. Por favor, responde con 'mayor', 'menor' o 'igual'.")