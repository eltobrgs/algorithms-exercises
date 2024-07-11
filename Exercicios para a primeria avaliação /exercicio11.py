'''Escreva um programa que cria uma lista de duas dicmensões uTlizando List
Comprehsion e imprima a diagonal principal desta lista.'''
n = 3
matriz = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        matriz[i][j] = int(input(f"Digite o valor da posição ({i}, {j}): "))
print("Diagonal principal:")
for i in range(n):
    print(matriz[i][i], end=" ")
