'''
• Crie um programa que utiliza um dicionário para guardar os dados de
um contato (nome, telefone, endereço e e-mail).
• O programa deverá permitir a inclusão de 5 contatos e depois
imprimir os dados desses contatos.
'''

import pprint
lista = []  # Cria uma lista vazia para armazenar os contatos

# Solicita ao usuário que insira os detalhes do contato 5 vezes
for i in range(2):
    print(" Digite as informaçoes do usuario de indice:", i+1)
    nome = input("Digite o nome: ")  # Solicita o nome
    telefone = input("Digite o telefone: ")  # Solicita o número de telefone
    endereco = input("Digite o endereço: ")  # Solicita o endereço
    email = input("Digite o email: ")  # Solicita o email
    
    # Cria um dicionário para armazenar os detalhes do contato
    contato = {'nome': nome, 'telefone': telefone, 'endereco': endereco, 'email': email}

    # Adiciona o dicionário de contato à lista
    lista.append(contato)

# Imprime os detalhes de cada contato na lista
# for contato in lista:
#     print(contato)

pprint.pprint(lista)  # Imprime os detalhes de cada contato na lista de forma mais organizada