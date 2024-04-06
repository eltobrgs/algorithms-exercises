a = [5, 3, 8, 1, 9, 2, 7, 4, 6, 10, 14, 11, 13, 12, 15]

# Inicializa as variáveis 'menor' e 'maior' com o primeiro elemento da lista 'a'
menor = a[0]
maior = a[0]

# Itera sobre cada elemento 'i' na lista 'a'
for i in a:
    # Verifica se o elemento atual 'i' é menor que o menor elemento atual 'menor'
    if i < menor:
        menor = i  # Atualiza o valor de 'menor' se 'i' for menor

    # Verifica se o elemento atual 'i' é maior que o maior elemento atual 'maior'
    if i > maior:
        maior = i  # Atualiza o valor de 'maior' se 'i' for maior

# Imprime os elementos menor e maior
print('Menor elemento:', menor)
print('Maior elemento:', maior)