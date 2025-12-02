"""Escriba un programa que calcula el salario neto semanal de un trabajador en función del 
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto"""

print("Introduce el nombre del trabajador")
nombre = input()
print("Introduce la cantidad de horas trabajadas en la semana")
horas_trabajadas = float(input())
print("Introduce la tarifa por hora")
tarifa_hora = float(input())
if horas_trabajadas <=35:
    salario_bruto = horas_trabajadas * tarifa_hora
else:
    horas_extra = horas_trabajadas - 35
    salario_bruto = (horas_trabajadas * tarifa_hora) + (horas_extra * tarifa_hora * 1.5)
if salario_bruto <= 500:
    tasa_impuesto = 0
elif salario_bruto <= 900:
    tasa_impuesto = (salario_bruto -500) * 0.25
else:
    tasa_impuesto = (400 *0.25) + ((salario_bruto - 900) * 0.45)
salario_neto = salario_bruto - tasa_impuesto
print(f"Nombre del trabajador: {nombre}")
print(f"Salario bruto: {salario_bruto} euros")
print(f"Tasa de impuesto: {tasa_impuesto} euros")
print(f"Salario neto: {salario_neto} euros")
