"""Escriba un programa que pida la edad por teclado y nos muestra el mensaje de “Eres mayor
de edad”, si y solamente si lo somos"""

print("Introduce tu edad:")
edad = int(input())
if edad >= 18:
    print("Eres mayor de edad")