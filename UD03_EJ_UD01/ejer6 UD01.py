"""Dibuja un ordinograma que dado el precio de un artículo y el precio de venta real nos
muestre el porcentaje de descuento realizado"""

print("Introduce el precio del artículo:")
precio_articulo= float(input())
print("Introduce el precio de venta real:")
precio_venta_real= float(input())
descuento= ((precio_articulo - precio_venta_real) / precio_articulo) * 100
print("El porcentaje de descuento realizado es:", descuento, "%")
