'''
Desenvolva um programa que leia dez números reais em uma lista A.
Construir uma lista B, observando a seguinte lei de formação: se o
valor do índice da Lista A for par, o valor deve ser multiplicado por 5;
sendo ímpar, deve ser somado por 5. Ao final, mostrar o conteúdo da
lista A e B.

2. Desenvolver um programa que leia cinco números inteiros de uma
lista A. No final, apresentar o total da soma dos elementos da lista A
que sejam ímpares.
'''

# Criar listas vazias A e B
a = []
b = []

# Ler dez números reais e preencher a lista A
for i in range(1, 11):
    a.append(float(input("Digite um número real: ")))

    # Verificar se o número no índice i-1 da lista A é par ou ímpar
    if a[i-1] % 2 == 0:
        # Se for par, adicionar 5 ao número e adicioná-lo à lista B
        b.append(a[i-1] + 5)
    else:
        # Se for ímpar, multiplicar o número por 5 e adicioná-lo à lista B
        b.append(a[i-1] * 5)

# Imprimir o conteúdo das listas A e B
print("Lista A:", a)
print("Lista B:", b)
