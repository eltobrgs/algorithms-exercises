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
    
    if cpf_valido(cpf_organizador) == "CPF inválido.":
        print("CPF inválido!")
        return
    
    data_evento = input("Digite a data do evento: ")
    horario_evento = input("Digite o horário do evento: ")
    local_evento = input("Digite o local do evento: ")
    vagas_evento = int(input("Digite a quantidade de vagas disponíveis: "))

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

    lista_eventos.append(evento)
    print("Evento cadastrado com sucesso!")

def listar_eventos():
    for i, evento in enumerate(lista_eventos, start=1):
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

    if cpf_valido(cpf_participante) == "CPF inválido.":
        print("CPF inválido!")
        return
    
    evento_escolhido = int(input("Digite o número do evento que deseja participar: "))
    
    if 1 <= evento_escolhido <= len(lista_eventos):
        evento = lista_eventos[evento_escolhido - 1]
        
        if evento['vagas'] > 0:
            participante = {
                'nome': nome_participante,
                'cpf': cpf_participante,
                'evento': evento['nome']
            }
            lista_participantes.append(participante)
            evento['vagas'] -= 1
            print("Participante cadastrado com sucesso!")
        else:
            print("Vagas esgotadas!")
    else:
        print("Evento não encontrado!")\
        
def listar_participantes():
    for i, participante in enumerate(lista_participantes, start=1):
        print(f"{i}-Participante:")
        print(f"Nome: {participante['nome']}")
        print(f"CPF: {participante['cpf']}")
        print(f"Evento: {participante['evento']}")
        print("")



def excluir_participante():
    listar_participantes()
    participanteexcluir = int(input('Digite o índice do participante do evento que deseja excluir: '))
    if 0 < participanteexcluir <= len(lista_participantes):
        # Remove o participante do evento da lista de participante do eventos
        lista_participantes.pop(participanteexcluir - 1)
        print('participante do evento excluído com sucesso!')
    else:
        print('Índice inválido!')


def excluir_evento():
    listar_eventos()
    eventoexcluir = int(input('Digite o índice do evento que deseja excluir: '))
    if 0 < eventoexcluir <= len(lista_eventos):
        lista_eventos.pop(eventoexcluir - 1)
        print('Evento excluído com sucesso!')
    else:
        print('Índice inválido!')
    