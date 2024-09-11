
def cpf_valido(cpf):
    # Verifica se o CPF tem 11 dígitos e se todos são números
    if len(cpf) != 11 or not cpf.isdigit():
        return "CPF inválido."
    else:
        # Converte o CPF em uma lista de inteiros
        cpf = [int(digit) for digit in cpf]

        # Verifica se todos os caracteres são dígitos
        is_valid = True
        for digit in cpf:
            if digit < 0 or digit > 9:
                is_valid = False
                break

        if is_valid:
            # Calcula o primeiro dígito verificador
            soma1 = 0
            for i in range(9):
                soma1 += cpf[i] * (10 - i)
            digito1 = (soma1 * 10 % 11) % 10

            # Calcula o segundo dígito verificador
            soma2 = 0
            for i in range(10):
                soma2 += cpf[i] * (11 - i)
            digito2 = (soma2 * 10 % 11) % 10

            # Verifica se os dígitos calculados são iguais aos fornecidos
            if digito1 == cpf[9] and digito2 == cpf[10]:
                return "CPF válido."
            else:
                return "CPF inválido."
        else:
            return "CPF inválido."


# yan, aqui eu determino a quantidade de vagas para cada dia e refeição
limite_vagas = {
    'segunda': {'almoço': 50, 'jantar': 30},
    'terça': {'almoço': 50, 'jantar': 30},
    'quarta': {'almoço': 50, 'jantar': 30},
    'quinta': {'almoço': 50, 'jantar': 30},
    'sexta': {'almoço': 50, 'jantar': 30},
}

# aqui eu determino a quantidade de vagas ocupadas para cada dia e refeição, inicia com 0
vagas_ocupadas = {
    'segunda': {'almoço': 0, 'jantar': 0},
    'terça': {'almoço': 0, 'jantar': 0},
    'quarta': {'almoço': 0, 'jantar': 0},
    'quinta': {'almoço': 0, 'jantar': 0},
    'sexta': {'almoço': 0, 'jantar': 0},
}

lista_alunos = []

def cadastrar_aluno():
    nome = input('Digite o nome do aluno: ').capitalize()
    cpf = input('Digite o CPF do aluno: ')
    dia = input('Digite o dia que deseja agendar: (segunda, terça, quarta, quinta, sexta): ')
    refeicao = input('Digite a refeição que deseja agendar (ex: almoço, jantar): ')
    # peço as informações do aluno, email, telefone, cpf, dia e refeição

    # vejo se o cpf é valido com a função que foi feita em um dos exercicios anteriores de messias
    if cpf_valido(cpf) == 'CPF inválido.':
        print('CPF inválido.')
        return
    else:
        # se o cpf for valido, eu verifico se a quantidade de vagas para o dia e refeição escolhidos já foram preenchidas, se o dia e refeição escolhidos já tiverem atingido o limite de vagas, eu fa.lo que as vagas estão esgotadas
        if vagas_ocupadas[dia][refeicao] >= limite_vagas[dia][refeicao]:
            print('Vagas esgotadas para esse dia e refeição!')
            return
        else:
            vagas_ocupadas[dia][refeicao] += 1
            # se ainda tiver vagas, eu adiciono 1 a quantidade de vagas ocupadas para o dia e refeição escolhidos


            # aqui eu crio um dicionario com as informações do aluno e adiciono a lista de alunos
            aluno = {'nome': nome, 
                    'cpf': cpf,
                    'dia': dia, 
                    'refeicao': refeicao}
            
            # e adiciono o dicionario a lisra de alunos com o metodo append, que adiciona um item a lista
            lista_alunos.append(aluno)
            print('Aluno cadastrado com sucesso!')

# ssa função lista os alunos cadastrados, se não houver alunos cadastrados, exibe a mensagem, se houver alunos cadastrados, exibe as informações deles
def listar_alunos():
    if len(lista_alunos) == 0: # se a quantidade de alunos na lista for igual a 0, exibimos a mensagem
        print('Nenhum aluno cadastrado!')
        return
    
    else:# se houver alunos na lista, exibimos as informações deles com um loop iterando sobre a lista de alunos, ou seja, para cada aluno na lista de alunos, exibimos as informações dele
        print('Listando alunos...')
        print('Lista de alunos que agendaram:')
        for indice, aluno in enumerate(lista_alunos, start=1): # dentro desse loop inicializamos as variáveis indice e aluno, o indice é o índice do aluno na lista de alunos e o aluno é o dicionario que contem as informações do aluno, usamos o método enumerate para obter o índice do aluno na lista e exibimos as informações do aluno, usamos o start=1 para começar a contagem do índice em 1

            print('-'*50)
            print(f"{indice}- Aluno: {aluno['nome']}, CPF: {aluno['cpf']}")
            print(f"Dia agendado: {aluno['dia']}, Refeição: {aluno['refeicao']}")
            print('-'*50)

        print('Listando total de alunos...') 
        total_alunos = len(lista_alunos) #aqui eu conto a quantidade de alunos na lista de alunos usando o método len, que retorna o tamanho da lista em numeros inteiros   
        print(f'Total de alunos que agendaram: {total_alunos}')   
        print('-'*50)


def listar_alunos_por_refeicao():
    refeicao = input('Digite a refeição que deseja listar (ex: almoço, jantar): ')
    alunos_refeicao = [] # crio uma lista vazia para armazenar os alunos que agendaram a refeição escolhida

    for aluno in lista_alunos: # para cada aluno na lista de alunos, verifico se a refeição agendada é igual a refeição escolhida
        if aluno['refeicao'] == refeicao: # se a refeição agendada for igual a refeição escolhida, eu adiciono o aluno a lista de alunos que agendaram a refeição escolhida
            alunos_refeicao.append(aluno)

    if len(alunos_refeicao) == 0:
        # se a quantidade de alunos na lista de alunos que agendaram a refeição escolhida for igual a 0, exibo a mensagem, ou seja, se nenhum aluno agendou a refeição escolhida, exibo a mensagem
        print('Nenhum aluno agendou essa refeição!')
        return
    
    else: # se houver alunos na lista de alunos que agendaram a refeição escolhida, exibo as informações deles
        print(f'Listando alunos que agendaram {refeicao}...')
        for aluno in alunos_refeicao: # para cada aluno na lista de alunos que agendaram a refeição escolhida, exibo as informações dele
            print('-'*50)
            print(f"Aluno: {aluno['nome']}, CPF: {aluno['cpf']}")
            print(f"Dia agendado: {aluno['dia']}, Refeição: {aluno['refeicao']}")
            print('-'*50)
        print('Listando total de alunos...') 
        total_alunos = len(alunos_refeicao)  #aqui eu conto a quantidade de alunos na lista de alunos por refeiçao usando o método len, que retorna o tamanho da lista em numeros inteiros
        print(f'Total de alunos que agendaram {refeicao}: {total_alunos}')   
        print('-'*50)


def excluir_aluno():
    # lista os alunos cadastrados
    listar_alunos()

    aluno_exclude = int(input('Digite o índice do aluno que deseja excluir: '))

    if 0 < aluno_exclude <= len(lista_alunos): # Verifica se o índice fornecido é válido, no caso de um índice inválido ele existe entre 0 e o tamanho da lista de alunos
        aluno_exclude -= 1 # Subtrai 1 para alinhar com o índice da lista, pois o índice fornecido pelo usuário começa em 1, mas o índice da lista começa em 0
        # Atualiza a quantidade de vagas ocupadas
        dia = lista_alunos[aluno_exclude]['dia']
        refeicao = lista_alunos[aluno_exclude]['refeicao']
        vagas_ocupadas[dia][refeicao] -= 1  # subtraímos 1 da quantidade de vagas ocupadas para o dia e refeição do aluno que está sendo excluído, pois a vaga que ele ocupava foi liberada

        # Remove o aluno da lista
        lista_alunos.pop(aluno_exclude -1) # usa o método pop para remover o aluno da lista de alunos, subtraímos 1 do índice fornecido para obter o índice correto do aluno na lista de alunos
        print('Aluno excluído com sucesso!')
    else:
        print('Índice inválido.')


def pesquisar_aluno():
    cpf_pesquisar = input('Digite o CPF do aluno que deseja pesquisar: ')
    aluno_encontrado = False # crio uma variável para verificar se o aluno foi encontrado, ela começa como False e posteriormente será alterada para True se o aluno for encontrado
    
    for aluno in lista_alunos: # para cada aluno na lista de alunos, verifico se o cpf do aluno é igual ao cpf que o usuário deseja pesquisar, se sim, exibo as informações do aluno e altero a variável aluno_encontrado para True
        if aluno['cpf'] == cpf_pesquisar:
            print('-'*50)
            print(f"Aluno encontrado: {aluno['nome']}, CPF: {aluno['cpf']}")
            print(f"Dia agendado: {aluno['dia']}, Refeição: {aluno['refeicao']}")
            print('-'*50)
            aluno_encontrado = True
            break

    if not aluno_encontrado: # se o aluno não for encontrado, a variável aluno_encontrado continuará como False e exibirei a mensagem de que o aluno não foi encontrado
        print('Aluno não encontrado!')