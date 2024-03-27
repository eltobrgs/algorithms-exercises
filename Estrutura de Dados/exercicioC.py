a = []  # Lista vazia para armazenar os números digitados pelo usuário em 'a'
b = []  # Lista vazia para armazenar os números digitados pelo usuário em 'b'
c = []  # Lista vazia para armazenar a diferença entre os números em 'a' e 'b'

for i in range(5):
    # Solicita ao usuário que digite um número inteiro para 'a' e o adiciona à lista 'a'
    a.append(int(input(f"Digite o {i+1}º número inteiro para 'a': ")))

    # Solicita ao usuário que digite um número inteiro para 'b' e o adiciona à lista 'b'
    b.append(int(input(f"Digite o {i+1}º número inteiro para 'b': ")))

    # Calcula a diferença entre o número correspondente em 'a' e 'b' e adiciona à lista 'c'
    c.append(a[i] - b[i])

# Imprime as listas 'a', 'b' e 'c'
print(a)
print(b)
print(c)
