a = [5, 3, 8, 1, 9, 2, 7, 4, 6, 10, 14, 11, 13, 12, 15]
print('Sem ordenação:', a)  # Imprime a lista original

for i in range(len(a)-1):  # Loop externo para percorrer a lista
    for j in range(1+i, len(a)):  # Loop interno para comparar os elementos
        if a[i] > a[j]:  # Verifica se o elemento atual é maior que o próximo
            a[i], a[j] = a[j], a[i]  # Troca os elementos de posição se necessário

print('Ordenado com bubble sort:', a)  # Imprime a lista ordenada usando o Bubble Sort

print('Ordenado em ordem decrescente com slice:', a[::-1])  # Imprime a lista ordenada em ordem decrescente usando o slice