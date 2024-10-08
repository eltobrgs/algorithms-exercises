def menu():
    print('SEJA BEM VINDO AO SISTEMA DE PETSHOP')
    print('1 - catalogo de serviços disponiveis')
    print('2 - cadastrar serviço')
    print('3 - cadastrar pet')
    print('4 - listar pets')
    print('5 - agendar serviço')
    print('6 - listar agendamentos')
    print('7 - cancelar serviço')
    print('8 - relatório de serviços')
    print('0 - sair do sistema')

# essa lista vai armazenar os serviços cadastrados, no caso os serviços que o petshop oferece para os clientes, como banho, tosa, etc
# a lista contem dicionarios com os seguintes campos: serv, preco, descricao
# eu deixei preenchido com dois serviços para caso queria testar o sistema
lista_serv = [
    {'serv': 'Banho', 'preco': 50.0, 'descricao': 'Banho completo para o seu pet.'},
    {'serv': 'Tosa', 'preco': 100.0, 'descricao': 'Tosa higiênica para seu pet.'},
    {'serv': 'Consulta', 'preco': 100.0, 'descricao': 'Consulta para seu pet.'}
]

lista_pets = []

lista_agendamentos = []

# essa função vai cadastrar um serviço no catalogo de serviços caso voce queira adicionar um novo serviço que o petshop vá a oferecer
def catalogar_serv():
    serv = input('Digite o nome do serviço: ').capitalize() #capitalize é um metodo que deixa a primeira letra da string em maiuscula
    preco = float(input('Digite o preço do serviço: '))
    descricao = input('Digite a descrição do serviço: ')
    # serv é o nome do serviço, preco é o preço do serviço e descricao é a descrição do serviço, vou usar esses valores para criar um dicionario que vai ser adicionado a lista_serv
    serv = {'serv': serv, 'preco': preco, 'descricao': descricao}
    lista_serv.append(serv)
    # o metodo append adiciona um item a lista, no caso o dicionario serv
    print('Serviço cadastrado com sucesso!')
    print('lista atualizada de serviços:')
    listar_serv()


def listar_serv():
    # essa função vai listar os serviços cadastrados, ela vai percorrer a lista de serviços e mostrar o nome do serviço, o preço e a descrição
    if len(lista_serv) == 0: # se a lista de serviços estiver vazia, exibe a mensagem, ou seja se o tamanho da lista for zero, ele exibe a mensagem
        print('Nenhum serviço cadastrado!')
        return
    else: # se a lista de serviços não estiver vazia, ele exibe a mensagem e percorre a lista de serviços
        print('Listando serviços...')
        for serv in lista_serv: # para cada serviço na lista de serviços, ele exibe o nome do serviço, o preço e a descrição
            indice = lista_serv.index(serv) + 1 # o indice é o numero do serviço na lista, eu adicionar +1 para começar do 1 e não do 0, ja que na vida real não existe o indice 0
            print(f"{indice}- Serviço: {serv['serv']}, Preço: {serv['preco']}, Descrição: {serv['descricao']}")

    # essa varivel indice vai ser usada para mostrar o indice do serviço na lista de serviços, o indice é o numero do serviço na lista, eu adicionar +1 para começar do 1 e não do 0, ja que na vida real não existe o indice 0

def cadastrar_pet():
    # exatamente a mesma logica do cadastro de serviço, só que agora para o cadastro de pets
    dono= input('Digite o nome do dono do pet: ').capitalize()
    nome = input('Digite o nome do pet: ').capitalize()
    raca = input('Digite a raça do pet: ').capitalize()
    idade = int(input('Digite a idade do pet: '))
    pet = {'dono': dono, 'nome': nome, 'raca': raca, 'idade': idade}
    lista_pets.append(pet)
    #lembrando que a lista de pets é uma lista de dicionarios, cada dicionario é um pet, e usamos o metodo .append para adicionar o dicionario pet a lista de pets
    print('Pet cadastrado com sucesso!')

def listar_pets():
    # extamente a mesma logica do listar serviços, só que agora para listar os pets
    if len(lista_pets) == 0: 
        print('Nenhum pet cadastrado!')
        return
    else:
        print('Listando pets...')
        for pet in lista_pets:
            indice = lista_pets.index(pet) + 1
            print(f" {indice}- Pet: {pet['nome']}, Raça: {pet['raca']}, Idade: {pet['idade']}")

def excluir_pet():
    listar_pets() #chama a função de listar pets
    pet_exclude = int(input('Digite o indice do pet que deseja excluir: '))
    lista_pets.pop(pet_exclude - 1) #.pop é um metodo que remove o item de uma lista dado o seu indice, o indice é passado como argumento para o metodo .pop 
    print('Pet excluido com sucesso!')
    

def agendar_servico():
    listar_pets() 
    listar_serv()

    nome_pet = input('Digite o nome do pet: ').capitalize()
    nome_serv = input('Digite o serviço desejado: ').capitalize()
    data = input('Digite a data do serviço: ')
    hora = input('Digite a hora do serviço: ')

    pet_encontrado = None
    for pet in lista_pets:  # para cada pet na lista de pets, ele verifica se o nome do pet é igual ao nome do pet que o usuario digitou
        if pet['nome'] == nome_pet:  # se o nome do pet estiver na lista de pets, o pet foi encontrado
            pet_encontrado = pet
            print('Pet encontrado!')
            break
    else:
        print('Pet não encontrado!')
        return

    serv_encontrado = None
    for serv in lista_serv:  # para cada serviço na lista de serviços, ele verifica se o nome do serviço é igual ao nome do serviço que o usuario digitou
        if serv['serv'] == nome_serv:
            serv_encontrado = serv
            print('Serviço encontrado!')
            break
    else:
        print('Serviço não encontrado!')
        return

    agendamento = {'pet': pet_encontrado['nome'], 'serv': serv_encontrado['serv'], 'data': data, 'hora': hora}
    lista_agendamentos.append(agendamento)
    # pega as informações do pet, serviço, data e hora e adiciona a lista de agendamentos
    # lembrando que a lista de agendamentos é uma lista de dicionarios, cada dicionario é um agendamento
    
    print('Agendando serviço...')
    print('Agendamento realizado com sucesso!')



def listar_agendamentos():
    if len(lista_agendamentos) == 0:  # se a lista de agendamentos estiver vazia, exibe a mensagem
        print('Nenhum agendamento realizado!')
        return
    else:  # se a lista de agendamentos não estiver vazia, ele exibe a mensagem e percorre a lista de agendamentos
        print('Listando agendamentos...')
        for agendamento in lista_agendamentos:  # para cada agendamento na lista de agendamentos, ele exibe o nome do pet, o serviço, a data e a hora
            indice = lista_agendamentos.index(agendamento) + 1  # o indice é o numero do agendamento na lista, eu adicionar +1 para começar do 1 e não do 0, ja que na vida real não existe o indice 0
            print(f"{indice}- Pet: {agendamento['pet']}, Serviço: {agendamento['serv']}, Data: {agendamento['data']}, Hora: {agendamento['hora']}")


def cancelar_servico():
    listar_agendamentos() #chama a função de listar agendamentos para o usuario ver os agendamentos que ele fez
    servico_exclude = int(input('Digite o indice do serviço que deseja cancelar: '))
    lista_agendamentos.pop(servico_exclude - 1)
    print('Serviço cancelado com sucesso!')


def relatoriodepets():
    if len(lista_agendamentos) == 0:
        print('Nenhum agendamento cadastrado!')
        return
    else:
    
        # Solicita ao usuário o índice do agendamento que deseja ver o relatório
        print('De qual agendamento deseja ver o relatório?')
        listar_agendamentos()
        agend_indice = int(input('Digite o índice do agendamento que deseja ver o relatório: '))

        # Verifica se o índice fornecido é válido
        if 0 < agend_indice <= len(lista_agendamentos):
            # Obtém o agendamento correspondente ao índice fornecido
            agendamento = lista_agendamentos[agend_indice - 1]

            # Exibe as informações do agendamento
            print(f"Pet: {agendamento['pet']}, Serviço: {agendamento['serv']}, Data: {agendamento['data']}, Hora: {agendamento['hora']}")
            for serv in lista_serv:
                if serv['serv'] == agendamento['serv']:
                    print(f'O preço do serviço é {serv["preco"]}')
                    break
            print('Relatório gerado com sucesso!')
            

            # Remove o agendamento da lista de agendamentos
            lista_agendamentos.pop(agend_indice - 1)
            print('Serviço concluído, excluindo do sistema!')
        else:
            print('Índice inválido!')


    