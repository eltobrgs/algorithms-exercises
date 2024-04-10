A = []  # Cria uma lista vazia chamada A
B = []  # Cria uma lista vazia chamada B

for i in range(12):  # Loop que executa 12 vezes
    num = int(input("Digite um número: "))  # Solicita ao usuário que digite um número e o converte para inteiro

    if num % 2 == 0:  # Verifica se o número é par
        A.append(num)  # Adiciona o número à lista A se for par
    elif num % 2 != 0:  # Verifica se o número é ímpar
        B.append(num)  # Adiciona o número à lista B se for ímpar

C = A + B  # Concatena as listas A e B para formar a lista C

print("Matriz A:", A)  # Imprime a lista A
print("Matriz B:", B)  # Imprime a lista B
print("Matriz C:", C)  # Imprime a lista C