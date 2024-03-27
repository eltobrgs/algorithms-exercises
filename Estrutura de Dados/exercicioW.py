# Defina os arrays A e B
A = []  # Array A para armazenar os números digitados pelo usuário
B = []  # Array B para armazenar os números digitados pelo usuário
C = []  # Array C para armazenar o resultado do cálculo

# Calcule o quadrado da soma dos elementos correspondentes em A e B
for i in range(10):
    A.append(int(input("Digite um número inteiro para A: ")))  # Solicita ao usuário um número inteiro para A e o adiciona ao array A
    B.append(int(input("Digite um número inteiro para B: ")))  # Solicita ao usuário um número inteiro para B e o adiciona ao array B
    C.append((A[i] ** 2 + B[i]) ** 2)  # Calcula o quadrado da soma dos elementos correspondentes em A e B e adiciona o resultado ao array C

# Imprima o array resultante C
print("lista resultante A:", A)  # Imprime o array A
print("lista resultante B:", B)  # Imprime o array B
print("lista resultante C:", C)  # Imprime o array C
