"""Programa que muestre en líneas separadas lo siguiente:
ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA,
WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A."""

for letra in range (ord("Z"), ord("A")-1, -1):
    for subletra in range (ord("Z"), letra-1, -1):
        print(chr(subletra), end="")
    print()