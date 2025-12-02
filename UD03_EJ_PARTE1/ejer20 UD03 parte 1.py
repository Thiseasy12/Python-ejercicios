"""Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la 
calificación alfabética, escribiendo el siguiente resultado (switch).
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente."""
print("Introduce una calificación entre 1 y 10")
calificaciones = float(input())
match calificaciones:
    case calificacion if 0 <= calificacion < 3:
        print("Muy Deficiente")
    case calificacion if 3 <= calificacion < 5:
        print("Insuficiente")
    case calificacion if 5 <= calificacion < 6:
        print("Suficiente")
    case calificacion if 6 <= calificacion < 7:
        print("Bien")
    case calificacion if 7 <= calificacion < 9:
        print("Notable")
    case calificacion if 9 <= calificacion <= 10:
        print("Sobresaliente")
    case _:
        print("Calificación inválida")