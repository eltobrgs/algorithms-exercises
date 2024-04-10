A = []  # Inicializa um array vazio

# Lê 10 elementos inteiros para o array
for i in range(10):
    num = int(input("Digite um número inteiro: "))
    A.append(num)

# Conta o número de elementos ímpares no array
adicionar = 0
for num in A:
    if num % 2 != 0:
        adicionar += 1
# Calcula a porcentagem de números ímpares
percentage = (adicionar / len(A)) * 100

# Imprime os resultados
print("Número total de elementos ímpares:", adicionar)
print("Porcentagem de números ímpares:", percentage)


