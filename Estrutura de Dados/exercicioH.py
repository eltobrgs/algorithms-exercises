a = []  # Cria uma lista vazia chamada 'a'
b = []  # Cria uma lista vazia chamada 'b'

for i in range(5):
    a.append(int(input("Digite um número real para lista a: ")))
    # Pede ao usuário para digitar um número real e o converte para inteiro antes de adicioná-lo à lista 'a'

a.sort()  # Ordena a lista 'a' em ordem crescente

b.append(sum(a))
# Adiciona à lista 'b' a soma de todos os elementos da lista 'a'

print(a)  # Imprime a lista 'a'
print(f'a somatoria da lista a é: {b}')
# Imprime a mensagem com a soma da lista 'a' usando uma f-string
