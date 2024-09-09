lista_eventos = []
lista_participantes = []

def cpf_valido(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido."
    else:
        cpf = [int(digit) for digit in cpf]
        
        # Verificação do primeiro dígito verificador
        soma1 = sum([cpf[i] * (10 - i) for i in range(9)])
        digito1 = (soma1 * 10 % 11) % 10
        
        # Verificação do segundo dígito verificador
        soma2 = sum([cpf[i] * (11 - i) for i in range(10)])
        digito2 = (soma2 * 10 % 11) % 10

        if digito1 == cpf[9] and digito2 == cpf[10]:
            return "CPF válido."
        else:
            return "CPF inválido."

def cadastrar_evento():
    nome_evento = input("Digite o nome do evento: ")
    descricao_evento = input("Digite a descrição do evento: ")
    nome_organizador = input("Digite o nome do organizador: ")
    cpf_organizador = input("Digite o CPF do organizador: ")
    # pedimos para o usuário digitar o nome, descrição, nome e cpf do organizador do evento
    
    # chamamos a funçao de verificar se o cpf é válido
    # se o cpf for inválido, exibimos a mensagem e retornamos da funçao
    if cpf_valido(cpf_organizador) == "CPF inválido.":
        print("CPF inválido!")
        return
    
    # se o cpf for válido, pedimos para o usuário digitar a data, horário, local e a quantidade de vagas disponíveis para o evento
    else:
        data_evento = input("Digite a data do evento: ")
        horario_evento = input("Digite o horário do evento: ")
        local_evento = input("Digite o local do evento: ")
        vagas_evento = int(input("Digite a quantidade de vagas disponíveis: "))

        # criamos um dicionário com as informações do evento e adicionamos à lista de eventos
        evento = {
            'nome': nome_evento,
            'descricao': descricao_evento,
            'organizador': nome_organizador,
            'cpf_organizador': cpf_organizador,
            'data': data_evento,
            'horario': horario_evento,
            'local': local_evento,
            'vagas': vagas_evento
        }

        # usamos o método append para adicionar o evento à lista de eventos
        lista_eventos.append(evento)
        print("Evento cadastrado com sucesso!")



def listar_eventos():
    for i, evento in enumerate(lista_eventos, start=1):
        # usamos o método enumerate para obter o índice do evento na lista e exibimos as informações do evento, usamos o start=1 para começar a contagem do índice em 1
        # se houver eventos na lista, exibimos as informações deles com um loop iterando sobre a lista de eventos, ou seja, para cada evento na lista de eventos, exibimos as informações dele
        print(f"{i}-Evento:{evento['nome']}")
        print(f"Organizador: {evento['organizador']}")
        print(f"CPF do organizador: {evento['cpf_organizador']}")
        print(f"Data: {evento['data']}")
        print(f"Horário: {evento['horario']}")
        print(f"Local: {evento['local']}")
        print(f"Vagas disponíveis: {evento['vagas']}")
        print("")



def cadastrar_participante():
    print("Lista de eventos disponíveis:")
    listar_eventos()  # Exibir lista de eventos antes de pedir o evento
    nome_participante = input("Digite o nome do participante: ")
    cpf_participante = input("Digite o CPF do participante: ")
    # pedimos para o usuário digitar o nome e o cpf do participante para poder participar do evento

    # chamamos a funçao de verificar se o cpf é válido
    if cpf_valido(cpf_participante) == "CPF inválido.":
        print("CPF inválido!")
        return
    # se ele for invalido retornamos da funçao
    # se ele for valido pedimos para o usuário digitar o número do evento que deseja participar
    else:
        evento_escolhido = int(input("Digite o número do evento que deseja participar: "))
        
        if 1 <= evento_escolhido <= len(lista_eventos): # Verificar se o evento escolhido existe, da seguinte forma: se o evento escolhido for maior ou igual a 1 e menor ou igual ao tamanho da lista de eventos ele existe
            evento = lista_eventos[evento_escolhido - 1]
            # fazemos evento = lista_eventos[evento_escolhido - 1] para obter o evento correto da lista de eventos
            # se nao fizessemos isso, o evento escolhido seria o número do evento - 1, pois a lista começa com o índice 0
            

            '''Entendimento da Indexação:
                As listas em Python utilizam indexação zero-based (baseada em 0), ou seja, o primeiro elemento da lista tem índice 0, o segundo tem índice 1, e assim por diante.
                Quando o usuário escolhe um evento, ele normalmente insere um número a partir de 1 (pois, na perspectiva do usuário, o primeiro item da lista é o número 1).
                No entanto, o índice do primeiro elemento da lista é 0. Portanto, para alinhar a escolha do usuário (que está inserindo 1 para o primeiro evento) com a indexação real da lista, subtraímos 1 da escolha do usuário.'''
            

            if evento['vagas'] > 0: # Verificar se há vagas disponíveis, se houver vagas disponíveis, adicionamos o participante ao evento
                participante = {
                    'nome': nome_participante,
                    'cpf': cpf_participante,
                    'evento': evento['nome']
                }

                lista_participantes.append(participante)
                evento['vagas'] -= 1 # Diminuir a quantidade de vagas disponíveis
                print("Participante cadastrado com sucesso!")
            else:
                print("Vagas esgotadas!")
        else:
            print("Evento não encontrado!")
        
def listar_participantes():
    # se a quantidade de participantes for igual a 0, exibimos a mensagem
    if len(lista_participantes) == 0:
        print("Nenhum participante cadastrado.")
    
    # se a quantidade de participantes for diferente de 0, exibimos as informações dos participantes
    else:
        for i, participante in enumerate(lista_participantes, start=1): # se houver participantes na lista, exibimos as informações deles com um loop iterando sobre a lista de participantes, ou seja, para cada participante na lista de participantes, exibimos as informações dele
            # usamos o método enumerate para obter o índice do participante na lista e exibimos as informações do participante, usamos o start=1 para começar a contagem do índice em 1
            print(f"{i}-Participante:")
            print(f"Nome: {participante['nome']}")
            print(f"CPF: {participante['cpf']}")
            print(f"Evento: {participante['evento']}")
            print("")



def excluir_participante():
    # chamamos a funçao de listar participantes para exibir os participantes do evento antes de pedir o participante
    listar_participantes()

    participanteexcluir = int(input('Digite o índice do participante do evento que deseja excluir: '))
    
    if 0 < participanteexcluir <= len(lista_participantes):# Verificar se o índice do participante a ser excluído é válido, da seguinte forma: se o índice do participante a ser excluído for maior que 0 e menor ou igual ao tamanho da lista de participantes, ele é válido
        # Remove o participante do evento da lista de participante do eventos
        lista_participantes.pop(participanteexcluir - 1)
        # usa o método pop para remover o participante do evento da lista de participantes do evento
        print('participante do evento excluído com sucesso!')
    else:
        print('Índice inválido!')


def excluir_evento():
    # mesma coisa que a funçao de excluir participante, mas para eventos
    listar_eventos()
    eventoexcluir = int(input('Digite o índice do evento que deseja excluir: '))
    if 0 < eventoexcluir <= len(lista_eventos):
        lista_eventos.pop(eventoexcluir - 1)
        print('Evento excluído com sucesso!')
    else:
        print('Índice inválido!')
    

def listar_participante():
    cpf_participante = input("Digite o CPF do participante: ")
    # pedimos para o usuário digitar o cpf do participante para exibir as informações dele
    for participante in lista_participantes:
        if cpf_participante in [participante['cpf']]:
            print("Participante encontrado:", participante)
            return
        else:
            print('participante nao encontrado na lista de participantes')

def listar_evento():
    nome_evento = input("Digite o nome do evento: ")
    # pedimos para o usuário digitar o cpf do participante para exibir as informações dele
    for evento in lista_eventos:
        if nome_evento in [evento['nome']]:
            print("evento encontrado:", evento["nome"])

            if evento['vagas'] > 0:
                print(f"Vagas disponíveis: {evento['vagas']}") 
                
                resp= input("Gostaria de se inscrever no evento? S/N").capitalize()
                if resp =="S":
                    cadastrar_participante()
                else:
                    print("OK!")
                    print('saindo do sistema...' )
                    break
        else:
            print('evento nao encontrado na lista de evento ')
    
    