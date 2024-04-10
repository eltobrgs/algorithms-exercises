a = []  # Cria uma lista vazia chamada 'a'
b = []  # Cria uma lista vazia chamada 'b'

for i in range(5):
    a.append(int(input("Digite um número real para lista a: ")))
    # Solicita ao usuário que digite um número real e o converte para inteiro antes de adicioná-lo à lista 'a'

    somatorio = 0  # Inicializa a variável 'somatorio' com o valor zero

    for j in range(a[i] + 1):
        somatorio *= j
        # Multiplica o valor atual de 'somatorio' pelo valor de 'j' em cada iteração do loop interno

    b.append(somatorio)
    # Adiciona o valor final de 'somatorio' à lista 'b'

print(a)  # Imprime a lista 'a'
print(b)  # Imprime a lista 'b'