'''Escreva um programa que leia uma lista de 15 posições de inteiros. Em seguida,
o programa deve ler um valor inteiro e imprimir o número de vezes que este
valor ocorre na lista.'''
lista = []
for i in range(5):
    lista.append(int(input(f"Digite o {i + 1}º número: "))
)
valor = int(input("Digite o valor a ser pesquisado: "))
print(f"O valor {valor} ocorre {lista.count(valor)} vezes na lista")