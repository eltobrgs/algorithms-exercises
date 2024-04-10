A = []  # Inicializa uma lista vazia

# Lê 10 elementos inteiros na lista
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    A.append(num)

# Conta o número de valores pares e ímpares
contagem_pares = 0
contagem_impares = 0

for num in A:
    if num % 2 == 0:
        contagem_pares += 1
    else:
        contagem_impares += 1

# Imprime os resultados
print("Número de valores pares:", contagem_pares)
print("Número de valores ímpares:", contagem_impares)