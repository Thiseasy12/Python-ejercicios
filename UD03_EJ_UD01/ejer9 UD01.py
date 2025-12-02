"""Dibuja un ordinograma de un programa que pida la edad por teclado y nos muestra el
mensaje de “Eres mayor de edad” o el mensaje de “Eres menor de edad”"""

print("Introduce tu edad:")
edad= int(input())
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    