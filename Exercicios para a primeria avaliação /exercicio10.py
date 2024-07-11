'''Escreva um programa em C que leia um lista de 20 inteiros, calcule e imprima:
a. A moda dos elementos na lista (elemento mais freqüente).
b. A mediana dos elementos no array (elemento central)
c. A média'''
lista = []
for i in range(5):
    lista.append(int(input(f"Digite o {i + 1}º número: ")))
moda = max(set(lista), key=lista.count)
print(f"A moda é {moda}")
lista.sort()
if len(lista) % 2 == 0:
    mediana = (lista[len(lista) // 2] + lista[len(lista) // 2 - 1]) / 2
else:
    mediana = lista[len(lista) // 2]
print(f"A mediana é {mediana}")
media = sum(lista) / len(lista)
print(f"A média é {media}")
