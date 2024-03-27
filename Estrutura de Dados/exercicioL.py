a = []  # Lista vazia para armazenar os números reais
b = []  # Lista vazia para armazenar os números reais elevados ao cubo

for i in range(5):
    a.append(int(input("Digite um número real: ")))  # Solicita ao usuário um número real e o adiciona à lista 'a'
    b.append(a[i] * (50/100))  # Calcula a metade do número atual e o adiciona à lista 'b'

print(a)  # Imprime a lista 'a' com os números reais digitados pelo usuário
print(b)  # Imprime a lista 'b' com os números reais elevados ao cubo
