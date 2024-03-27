# Definir a matriz A
A = []

# Ler os elementos da matriz
for i in range(15):
    elemento = int(input("Digite um número inteiro: "))
    A.append(elemento)

# Contar os elementos pares
total_pares = 0
for elemento in A:
    if elemento % 2 == 0:
        total_pares += 1

# Apresentar o total de elementos pares
print("O total de elementos pares na matriz é:", total_pares)