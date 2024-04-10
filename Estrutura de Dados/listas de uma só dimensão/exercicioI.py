a = []  # Cria uma lista vazia chamada 'a'
b = []  # Cria uma lista vazia chamada 'b'
c = []  # Cria uma lista vazia chamada 'c'
d = []  # Cria uma lista vazia chamada 'd'

for i in range(5):
    # Solicita ao usuário que digite um número real para a lista 'a' e o adiciona à lista
    a.append(int(input("Digite um número real para lista a: ")))

    # Solicita ao usuário que digite um número real para a lista 'b' e o adiciona à lista
    b.append(int(input("Digite um número real para lista b: ")))

    # Solicita ao usuário que digite um número real para a lista 'c' e o adiciona à lista
    c.append(int(input("Digite um número real para lista c: ")))

    d.append(a[i] + b[i] + c[i])  # Calcula a soma dos números correspondentes em 'a', 'b' e 'c' e adiciona à lista 'd'

print(d)  # Imprime a lista vazia 'd'