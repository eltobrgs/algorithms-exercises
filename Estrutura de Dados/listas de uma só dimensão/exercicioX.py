A = []  # Inicialize o array A
B = []  # Inicialize o array B
# Leia 6 elementos para o array A
for i in range(6):
    element = float(input(f"Digite o elemento {i+1} do array A: "))
    A.append(element)

# Construa o array B com base nas condições
for i in range(6):
    if i % 2 == 0:  # Índice par em B
        B.append(A[i+1])  # Atribua o elemento de índice ímpar de A
    else:  # Índice ímpar em B
        B.append(A[i-1])  # Atribua o elemento de índice par de A

# Imprima ambos os arrays
print("Array A:", A)
print("Array B:", B)