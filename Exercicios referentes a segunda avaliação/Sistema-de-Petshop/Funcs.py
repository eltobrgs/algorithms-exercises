def menu():
    print('SEJA BEM VINDO AO SISTEMA DE PETSHOP')
    print('1 - catalogo de serviços disponiveis')
    print('2 - cadastrar serviço')
    print('3 - cadastrar pet')
    print('4 - listar pets')
    print('5 - agendar serviço')
    print('6 - listar agendamentos')
    print('7 - cancelar serviço')
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
    serv = input('Digite o nome do serviço: ')
    preco = float(input('Digite o preço do serviço: '))
    descricao = input('Digite a descrição do serviço: ')
    # serv é o nome do serviço, preco é o preço do serviço e descricao é a descrição do serviço, vou usar esses valores para criar um dicionario que vai ser adicionado a lista_serv
    serv = {'serv': serv, 'preco': preco, 'descricao': descricao}
    lista_serv.append(serv)
    # o metodo append adiciona um item a lista, no caso o dicionario serv
    print('Serviço cadastrado com sucesso!')


def listar_serv():
    print('Listando serviços...')
    indice = lista_serv.index(serv) + 1
    # essa varivel indice vai ser usada para mostrar o indice do serviço na lista de serviços, o indice é o numero do serviço na lista, eu adicionar +1 para começar do 1 e não do 0, ja que na vida real não existe o indice 0
    for serv in lista_serv:
        print(f"{indice}- Serviço: {serv['serv']}, Preço: {serv['preco']}, Descrição: {serv['descricao']}")


def cadastrar_pet():
    # exatamente a mesma logica do cadastro de serviço, só que agora para o cadastro de pets
    dono= input('Digite o nome do dono do pet: ')
    nome = input('Digite o nome do pet: ')
    raca = input('Digite a raça do pet: ')
    idade = int(input('Digite a idade do pet: '))
    pet = {'dono': dono, 'nome': nome, 'raca': raca, 'idade': idade}
    lista_pets.append(pet)
    print('Pet cadastrado com sucesso!')

def listar_pets():
    # extamente a mesma logica do listar serviços, só que agora para listar os pets
    print('Listando pets...')
    for pet in lista_pets:
        indice = lista_pets.index(pet) + 1
        print(f" {indice}- Pet: {pet['nome']}, Raça: {pet['raca']}, Idade: {pet['idade']}")

def excluir_pet():
    listar_pets()
    pet_exclude = int(input('Digite o indice do pet que deseja excluir: '))
    lista_pets.pop(pet_exclude - 1) #.pop é um metodo que remove o item de uma lista dado o seu indice, o indice é passado como argumento para o metodo .pop 
    print('Pet excluido com sucesso!')

def agendar_servico():
    listar_pets()
    listar_serv()

    pet = input('Digite o nome do pet: ')
    serv = input('Digite o serviço desejado: ')
    data = input('Digite a data do serviço: ')
    hora = input('Digite a hora do serviço: ')

    for pet in lista_pets:
        if pet['nome'] == pet:
            print('Pet encontrado!')
            break

        # se o nome do pet esticer na lista de pets, o pet foi encontrado, se não, o pet não foi encontrado
    else:
        print('Pet não encontrado!')
        return
     # se o pet não foi encontrado, a função é encerrada


    # mesma logica do pet, só que agora para o serviço
    for serv in lista_serv:
        if serv['serv'] == serv:
            print('Serviço encontrado!')
            break
    else:
        print('Serviço não encontrado!')
        return
    
    agendamento= {'pet': pet, 'serv': serv, 'data': data, 'hora': hora}
    lista_agendamentos.append(agendamento)
    # pega as informações do pet, serviço, data e hora e adiciona a lista de agendamentos
    # lembrando que a lista de agendamentos é uma lista de dicionarios, cada dicionario é um agendamento
    
    print('Agendando serviço...')
    print('Agendamento realizado com sucesso!')


def listar_agendamentos():
    print('Listando agendamentos...')
    for agendamento in lista_agendamentos:
        indice = lista_agendamentos.index(agendamento) + 1
        print(f"{indice}- Pet: {agendamento['pet']}, Serviço: {agendamento['serv']}, Data: {agendamento['data']}, Hora: {agendamento['hora']}")

def cancelar_servico():
    listar_agendamentos()
    servico_exclude = int(input('Digite o indice do serviço que deseja cancelar: '))
    lista_agendamentos.pop(servico_exclude - 1)
    print('Serviço cancelado com sucesso!')
