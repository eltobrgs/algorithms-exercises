a = []  # Lista vazia para armazenar os números reais
b = []  # Lista vazia para armazenar os números reais elevados ao cubo

for i in range(5):
    a.append(int(input("Digite um número real: ")))  # Solicita ao usuário um número real e o adiciona à lista 'a'
    f = 1

    for c in range(1, int(a[i])+1):
        f *= c
    b.append(f)
print(a)  # Imprime a lista 'a' com os números reais digitados pelo usuário
print(b)  # Imprime a lista 'b' com os números reais elevados ao cubo
