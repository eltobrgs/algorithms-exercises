#usando a funçao factorial do modulo math, crie uma matriz 5x4 com numeros aleatorios de 1 a 10 e calcule o fatorial de cada numero
import random
import math
a = [[random.randint(1, 10) for j in range(4)] for i in range(5)]
b = [[math.factorial(a[i][j]) for j in range(4)] for i in range(5)]

for linha in a: 
    print('numeros', linha)
for linha in b:
    print('numeros fatorial', linha)

