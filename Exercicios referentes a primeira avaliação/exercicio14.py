# Pergunta o número limite ao usuário
limite = int(input("Digite um número inteiro: "))

# Inicializa uma lista para armazenar os números primos
primos = []

# Itera por todos os números de 2 até o limite (1 não é primo)
for num in range(2, limite + 1):
    # Assume que o número é primo
    is_primo = True
    # Verifica se o número é divisível por algum número menor que ele
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_primo = False
            break
    # Se o número é primo, adiciona à lista de primos
    if is_primo:
        primos.append(num)

# Exibe a lista de números primos
print("Números primos entre 1 e", limite, "são:", primos)
