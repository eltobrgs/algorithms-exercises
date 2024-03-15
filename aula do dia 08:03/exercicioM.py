soma_total = 0  # Variável para armazenar a soma dos fatoriais

for K in range(10):  # Loop que executa 15 vezes
    numero = int(input("Digite um número: "))  # Solicita ao usuário que digite um número e o converte para inteiro
    fatorial = 1  # Variável para armazenar o fatorial do número

    for i in range(1, numero + 1):  # Loop que calcula o fatorial do número
        fatorial *= i  # Multiplica o fatorial pelo valor atual de i

    soma_total += fatorial  # Adiciona o fatorial calculado à soma total

print("A soma dos fatoriais é:", soma_total)  # Imprime a soma dos fatoriais

result = (soma_total)/K
print(result)