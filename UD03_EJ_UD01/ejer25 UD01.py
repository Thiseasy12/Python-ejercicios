"""Dibuja un ordinograma que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado.
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente"""

print("Introduce una calificación numérica entre 0 y 10:")
calificacion = float(input())
if 0 <= calificacion < 3:
    print("Muy Deficiente")
elif 3 <= calificacion < 5:
    print("Insuficiente")
elif 5 <= calificacion < 6:
    print("Suficiente")
elif 6 <= calificacion < 7:
    print("Bien")
elif 7 <= calificacion < 9:
    print("Notable")
elif 9 <= calificacion <= 10:
    print("Sobresaliente")