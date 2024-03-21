'''Desenvolva um programa que leia dez números reais em uma lista
A. Construir um lista B, observando a seguinte lei de formação: se o
valor d índice da Lista A for par, o valor deve ser multiplicado por 5;
sendo impar deve se somado por 5. Ao final mostrar o conteúdo da
lista A e B.
2. Desenvolver um programa que leia cinco números inteiro de uma
lista A. No final, apresentar o total da soma dos elementos da lista A
que sejam impares.'''

a = []
b = []

for i in range(1, 11):
    a.append(float(input("Digite um número real: ")))
    if a[i-1] % 2 == 0:
        b.append(a[i-1] * 5)
    else:
        b.append(a[i-1] + 5)

print("Lista A:", a)
print("Lista B:", b)

sum_of_odds = sum([num for num in a if num % 2 != 0])
print("Soma dos números ímpares da lista A:", sum_of_odds)