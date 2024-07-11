'''Escreva um programa que recebe um CNPJ e verifica se ele é válido e inváido.'''
cnpj = input("Digite o CNPJ: ")
cnpj = cnpj.replace(".", ""); cnpj = cnpj.replace("/", ""); cnpj = cnpj.replace("-", "")

if len(cnpj) != 14:
    print("CNPJ inválido")
else:
    print("CNPJ válido")