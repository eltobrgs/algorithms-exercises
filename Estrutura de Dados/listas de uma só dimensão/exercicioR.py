A = []  # Lista vazia para armazenar os números da matriz A
B = []  # Lista vazia para armazenar os números da matriz B
C = []  # Lista vazia para armazenar os números da matriz C
D = []  # Lista vazia para armazenar os números da matriz D

for i in range(6):
    A.append(int(input("Digite um número para a matriz A: ")))  # Solicita um número para a matriz A e o adiciona à lista A
    B.append(int(input("Digite um número para a matriz B: ")))  # Solicita um número para a matriz B e o adiciona à lista B
    
    if i % 2 != 0:  # Verifica se o índice é ímpar
        C.append(A[i])  # Adiciona o número da matriz A com o índice ímpar à lista C
        C.append(B[i])  # Adiciona o número da matriz B com o índice ímpar à lista C
    else:  # Caso contrário, o índice é par
        D.append(A[i])  # Adiciona o número da matriz A com o índice par à lista D
        D.append(B[i])  # Adiciona o número da matriz B com o índice par à lista D

print("Matriz C:", C)  # Imprime a lista C, que contém os números com índices ímpares
print("Matriz D:", D)  # Imprime a lista D, que contém os números com índices pares