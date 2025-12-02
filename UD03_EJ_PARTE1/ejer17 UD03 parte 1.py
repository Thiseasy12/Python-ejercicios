"""Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y 
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario 
incorrecto"""

print("Dame el noombre de usuario")
usuario = input()
print("Dame la contraseña")
contraseña = input()
if usuario == "Juan" and contraseña == "123456":
    print ("Inicio de sesion correcto")
else:
    print ("Nombre de usuario incorrecto")

