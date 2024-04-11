# Inicializando a matriz A
A = [i for i in range(1, 11)]

# Inicializando a matriz B
B = []

for i in A:
    linha = []
    linha.append(i + 5)
    
    # Calculando o fatorial
    fatorial = 1
    for j in range(1, i + 1):
        fatorial *= j
    linha.append(fatorial)
    
    linha.append(i**2)
    B.append(linha)

# Imprimindo a matriz B
for linha in B:
    print(linha)