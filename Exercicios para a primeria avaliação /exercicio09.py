'''Escreva um programa que leia uma lista de 10 posições ordenados de inteiros e
um inteiro. O programa deve informar a primeira posição onde este inteiro
ocorre no vetor ou False caso o valor não ocorra na lista (Busca Binária).'''

lista = []
for i in range(5):
    lista.append(int(input(f"Digite o {i + 1}º número: ")))
valor = int(input("Digite o valor a ser pesquisado: "))
inicio = 0
fim = len(lista) - 1
while inicio <= fim:
    posi = (inicio + fim) // 2
    if lista[posi] == valor:
        print(f"O valor {valor} ocorre na posição {posi}")
        break
    elif lista[posi] < valor:
        inicio = posi + 1
    else:
        fim = posi - 1
else:
    print("o valor não ocorre na lista")