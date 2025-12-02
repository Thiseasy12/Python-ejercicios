"""Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si 
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta” 
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo 
según sea el caso y el total a pagar de la compra"""

print("Ingresa el valor de la compra")
valor_compra = float(input())
print("Ingresa el metodo de pago (contado/tarjeta)")
metodo_pago = input().lower()
if metodo_pago == "contado":
    descuento = valor_compra * 0.05
    total_pagar = valor_compra - descuento
    print(f"Descuento aplicado:{descuento} euros")
    print(f"Total a pagar: {total_pagar} euros")
elif metodo_pago == "tarjeta":
    recargo = valor_compra * 0.03
    total_pagar = valor_compra + recargo
    print(f"Recargo aplicado: {recargo} euros")
    print(f"Total a pagar: {total_pagar} euros")
else:
    print("Método de pago inválido")
    