A = []  # Cria uma lista vazia chamada A
B = []  # Cria uma lista vazia chamada B

for i in range(10):  # Loop que executa 10 vezes
    num = int(input("Digite um número: "))  # Solicita ao usuário que digite um número e o converte para inteiro

    if num % 2 == 0 and num % 3 == 0:  # Verifica se o número é divisível por 2 e por 3
        A.append(num)  # Adiciona o número à lista A se for divisível por 2 e por 3

for i in range(10):  # Loop que executa 10 vezes
    num = int(input("Digite um número: "))  # Solicita ao usuário que digite um número e o converte para inteiro

    if num % 5 == 0:  # Verifica se o número é múltiplo de 5
        B.append(num)  # Adiciona o número à lista B se for múltiplo de 5

C = A + B  # Concatena as listas A e B para formar a lista C

print("Matriz A:", A)  # Imprime a lista A
print("Matriz B:", B)  # Imprime a lista B
print("Matriz C:", C)  # Imprime a lista C
