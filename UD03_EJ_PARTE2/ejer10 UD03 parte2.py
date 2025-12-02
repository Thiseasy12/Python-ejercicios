"""Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales"""
suma = 0
prudcuto = 1
for i in range(10):
    suma += i
    prudcuto *= i
    print(f"La suma de los primeros 10 numeros naturales es: {suma}")
    