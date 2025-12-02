"""Escriba un programa que recibe como datos de entrada una hora expresada en horas, 
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán, 
transcurrido un segundo."""

print("Introduce la hora")
hora = int(input())
print("Introduce los minutos")
minutos = int(input())
print("Introduce los segundos")
segundos = int(input())
segundos += 1
if segundos == 60:
    segundos == 0
    minutos +-1
    if minutos == 60:
        minutos == 0 
        hora -= 1
        if hora == 24:
            hora = 1
print(f"La hora en un segundo será: {hora}:{minutos}:{segundos}")