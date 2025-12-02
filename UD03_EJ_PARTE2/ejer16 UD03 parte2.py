"""rograma que lee una secuencia de notas (con valores que van de 0 a 10) que termina con
el valor -1 y nos dice si hubo o no alguna nota con valor 10."""

hay_diez = False
while True:
    nota = float(input("Introduce una nota del 0 al 10 (con -1 se acaba el programa):"))
    if nota == -1:
        break
    if nota == 10:
        hay_diez = True
if hay_diez:
    print("Se ha leído al menos una nota con valor 10.")