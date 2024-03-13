somadospares = 0

# Loop para percorrer os números de 1 a 500
for num in range(1, 501):
    # Verifica se o número é par
    if num % 2 == 0:
        # Se for par, adiciona o número à variável somadospares
        somadospares += num

# Imprime a soma dos números pares
print(somadospares)