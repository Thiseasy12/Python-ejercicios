"""Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos
la altura de la pirámide por teclado. """


altura = int(input("Introduce la altura de la piramide:"))
for i in range(altura,0,-1):
    print (" " * (altura -i) + "*" *(i *2 -1))
    