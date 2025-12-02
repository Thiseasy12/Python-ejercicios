"""En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis, mostrar el mensaje “Excelente”
Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
Si un dado se obtiene seis, mostrar el mensaje “Regular”
Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch)."""

print("Introduce el valor del primer dado:")
dado1 = int(input())
print("Introduce el valor del siguiente dado:")
dado2 = int(input())
print("Introduce el valor del último dado:")
dado3 = int(input())
dados_seis = 0
if dado1 == 6:
    dados_seis += 1
if dado2 == 6:
    dados_seis += 1
if dado3 == 6:
    dados_seis += 1
if dados_seis == 3:
    print("Excelente")
elif dados_seis == 2:
    print("Muy bien")
elif dados_seis == 1:
    print("Regular")
else:
    print("Pésimo")