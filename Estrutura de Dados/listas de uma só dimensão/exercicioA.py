a = []  # Cria uma lista vazia chamada 'a'
for i in range(0, 10):
    a.append(str(input("Digite o elemento: ")))  # Solicita ao usuário que digite um elemento e o adiciona à lista 'a'
print(a)  # Imprime a lista 'a'

a.reverse()  # Inverte a ordem dos elementos na lista 'a'
print(a)  # Imprime a lista 'a' novamente, agora com os elementos invertidos
