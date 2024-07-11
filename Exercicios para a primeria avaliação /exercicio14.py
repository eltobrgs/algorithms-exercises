'''Crie um programa que idenTfique se uma palavra é um palíndromo.'''

palavra = input("Digite uma palavra: ")
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
