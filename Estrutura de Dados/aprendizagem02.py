'''2. Desenvolver um programa que leia cinco números inteiro de uma
lista A. No final, apresentar o total da soma dos elementos da lista A
que sejam impares.'''
a = []
soma = 0

for i in range(0, 5):
    a.append(int(input(f"Digite o {i+1}º número inteiro: ")))
    if a[i] % 2 != 0:
        soma += a[i]

print(f"A soma dos números ímpares é: {soma}")
