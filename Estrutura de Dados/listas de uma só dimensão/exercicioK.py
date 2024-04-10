a = []  # Lista vazia para armazenar os números reais
b = []  # Lista vazia para armazenar os números reais elevados ao cubo

for i in range(5):
    a.append(int(input("Digite um número real: ")))  # Solicita ao usuário um número real e o adiciona à lista 'a'
    b.append(a[i] * -1)  # Calcula o negativo do número atual e o adiciona à lista 'b'
    if i in a and a[i] < 0:
        print("O número é negativo, VALOR INVALIDO")
        
else:
    print(a)  # Imprime a lista 'a' com os números reais digitados pelo usuário
    print(b)  # Imprime a lista 'b' com os números reais elevados ao cubo
