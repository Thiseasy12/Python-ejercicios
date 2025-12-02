"""Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares, 
con el siguiente menú de opciones: SWITCH"""

saldo = 1000
print("Bienvenido al nuevo cajero automatico")
print("Seleccione una opción:")
print("1. Ingresar dinero")
print("2. Retirar dinero")
print("3. Consultar saldo")
opcion = int(input())
match opcion:
    case 1:
        ingreso = float(input("Cantidad a ingresar: "))
        saldo += ingreso
        print(f"Nuevo saldo: {saldo}")
    case 2:
        retiro = float(input("Cantidad a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Nuevo saldo: {saldo} dólares.")
        else:
            print("Saldo insuficiente")
    case 3:
        print(f"Su saldo actual es: {saldo}")
    case _:
        print("Opción inválida")