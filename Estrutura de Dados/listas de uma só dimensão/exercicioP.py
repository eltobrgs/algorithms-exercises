a = []  # Lista vazia para armazenar os números digitados
b = []  # Lista vazia para armazenar os números modificados

for i in range(6):
    a.append(int(input("Digite um número real: ")))  # Solicita ao usuário que digite um número e o converte para inteiro

    if a[i] % 2 == 0:  # Verifica se o número é par
        a[i] = a[i] * 2  # Multiplica o número por 2 se for par
        b.append(a[i])  # Adiciona o número modificado à lista b
    else:
        b.append(a[i])  # Adiciona o número original à lista b se for ímpar

print(f"lista b: {b}")  # Imprime a lista b contendo os números modificados ou originais