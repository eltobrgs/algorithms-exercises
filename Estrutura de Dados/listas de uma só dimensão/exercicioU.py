

A = []  # Cria uma lista vazia chamada A
B = []  # Cria uma lista vazia chamada B

# Loop para preencher a matriz A com 10 valores
for i in range(10):
    value = int(input("Digite um valor para a matriz A: "))  # Solicita ao usuário um valor para a matriz A
    if value % 2 == 0 and value % 3 == 0:  # Verifica se o valor é divisível por 2 e 3
        A.append(value)  # Adiciona o valor à matriz A
    else:
        print("Entrada inválida. O valor deve ser divisível por 2 e 3.")
        i -= 1  # Reduz o contador do loop em 1 para repetir a iteração

# Loop para preencher a matriz B com 10 valores
for i in range(10):
    value = int(input("Digite um valor para a matriz B: "))  # Solicita ao usuário um valor para a matriz B
    if value % 5 == 0:  # Verifica se o valor é um múltiplo de 5
        B.append(value)  # Adiciona o valor à matriz B
    else:
        print("Entrada inválida. O valor deve ser um múltiplo de 5.")
        i -= 1  # Reduz o contador do loop em 1 para repetir a iteração

C = A + B  # Concatena as matrizes A e B para formar a matriz C

print("Matriz C:", C)  # Imprime a matriz C