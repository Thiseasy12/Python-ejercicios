"""Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre
el porcentaje de descuento realizado"""

print("Introduce el precio del articulo:")
precio_articulo = float(input())
print("Introduce el precio de venta real:")
precio_venta = float(input())

descuento = precio_articulo - precio_venta
porcentaje_descuento = (descuento / precio_articulo) * 100

print(f"El porcentaje de descuento realizado es: {porcentaje_descuento}%")