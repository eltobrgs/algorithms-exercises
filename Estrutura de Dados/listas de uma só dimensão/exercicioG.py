a = []  # Cria uma lista vazia chamada 'a'
b = []  # Cria uma lista vazia chamada 'b'
c = []  # Cria uma lista vazia chamada 'c'

# Preenche a lista 'a' com 5 números reais fornecidos pelo usuário
for i in range(5):
    a.append(int(input("Digite um número real para lista a: ")))

# Preenche a lista 'b' com 10 números reais fornecidos pelo usuário
for i in range(10):
    b.append(int(input("Digite um número real para lista b: ")))

c = a + b  # Concatena as listas 'a' e 'b' e atribui o resultado à lista 'c'

print(c)  # Imprime a lista 'c'