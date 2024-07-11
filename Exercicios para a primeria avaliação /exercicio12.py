''' Escreva um programa que recebe um CPF e verifica se ele é válido ou inválido.'''
cpf = input("Digite o CPF: ")
cpf = cpf.replace(".", ""); cpf = cpf.replace("-", "")

if len(cpf) != 11:

    print("CPF inválido")
else:
    print("CPF válido")
    