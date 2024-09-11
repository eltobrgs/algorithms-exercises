# importando a função sleep da biblioteca time
from time import sleep

lista_medicos = [] # lista medicos
lista_pacientes = [] # lista pacientes
lista_consultas = [] # lista consultas

# Função para verificar se um CPF é válido
# feito em grupo na sala
def cpf_valido(cpf):
    # Verifica se o CPF tem 11 dígitos
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

# Função para cadastrar médico 
# feito em grupo na sala mas modificado por mim, pensando em alguma situaçao que alguem tente cadastrar um medico que ja esta cadastrado
def cadastrar_medico():
    nome_medico = input("Digite o nome do médico: ").capitalize() #capitalize é um metodo que converte a primeira letra de uma string em maiúscula
    especialidade = input("Digite a especialidade: ")
    credencial_medico = input("Digite a credencial do médico: ")
    limite_atendimentos = int(input("Quantos pacientes o médico pode atender por dia: "))

    for medico in lista_medicos:
        if medico['credencial'] == credencial_medico: #se houver alguma credencial igual a credencial_medico, o medico ja foi cadastrado
            
            print("Médico já cadastrado no sistema!")
            
            return

    medico = {
        'nome': nome_medico,
        'credencial': credencial_medico,
        'especialidade': especialidade,
        'limite_atendimento': limite_atendimentos
    }

    lista_medicos.append(medico)
    print("Carregando...")
    sleep(1)
    
    print("Médico cadastrado com sucesso!")
    

# Função para listar médicos
# feito em grupo na sala mas modificado por mim, pensando em alguma situaçao que alguem tente listar medicos e suas especialidades
#  para mostrar os medicos disponiveis para um possivel paciente
def listar_medicos():
    print("Carregando médicos...")
    sleep(1)
    if not lista_medicos:
        
        print("Nenhum medico cadastrado no sistema!")
        
        return
    
    print('Medicos disponiveis:')
    for medico in lista_medicos:

        ''' O método .index(medico) percorre a lista internamente para encontrar o índice, 
        o que pode ser custoso se a lista for grande. Uma alternativa seria usar um enumerate, que atribui 
        o índice automaticamente: o método .index(medico) retorna o índice do médico atual dentro da lista lista_medicos.'''

        indice = lista_medicos.index(medico) + 1 
        
        print(f" {indice} - Médico: {medico['nome']}, Especialidade: {medico['especialidade']}")
        


def excluir_medico():
    listar_medicos()

    try:
        medico_exclude= int(input("Qual indice do medico que deseja excluir:"))
        if medico_exclude < 0 or medico_exclude > len(lista_medicos):
            print("Indice invalido")
            return 
        
        else:
            lista_medicos.pop(medico_exclude - 1) #.pop é um metodo que remove o item de uma lista dado o seu indice, o indice é passado como argumento para o metodo .pop
            # o -1 é para que o indice seja o mesmo que o usuario digitou, pois o indice começa em 0
            print("Medico excluido com sucesso!")
            

    except ValueError:
        print("Digite apenas o indice, não o nome do medico, ou qualquer outra credencial na lista")
    

# Função para cadastrar paciente
# feito em grupo na sala
def cadastrar_paciente():
    nome_paciente = input("Digite o nome do paciente: ").capitalize() #capitalize é um metodo que converte a primeira letra de uma string em maiúscula
    cpf_paciente = input("Digite o CPF do paciente (somentes numeros): ")

    # Verifica se o CPF é válido
    if not cpf_valido(cpf_paciente): #verifica se o cpf é valido, se não for, ele exibe a mensagem de que o cpf é invalido, ou seja, se a função cpf_valido retornar "false."
        
        print("CPF inválido, entre com um CPF válido!")
        
        return
    
    for paciente in lista_pacientes:
        if paciente['cpf_paciente'] == cpf_paciente: #itera em toda a lista de pacientes, olhando especificamente para o valor atribuido a "cpf_paciente" para verificar se o paciente ja esta cadastrado, se o for igual ao cpf_paciente que esta sendo cadastrado, o paciente ja foi cadastrado
            
            print("Paciente já cadastrado no sistema!")
            
            return
        
    email_paciente = input("Digite o email do paciente: ")
    paciente = {
        'nome_paciente': nome_paciente, 
        'cpf_paciente': cpf_paciente, 
        'email_paciente': email_paciente
    }
    
    lista_pacientes.append(paciente)
    print("Carregando...")
    sleep(1)
    
    print("Paciente cadastrado com sucesso!")
    


# Função para listar pacientes
# feito por mim para alguam situaçao que alguem tente listar os pacientes cadastrados no sistema para saber quem ja esta cadastrado
def listar_pacientes():
    print("Carregando pacientes...")
    sleep(1)
    if not lista_pacientes: #se a lista de pacientes estiver vazia, ele exibe a mensagem de que não há pacientes cadastrados no sistema
        
        print("Nenhum paciente cadastrado no sistema!")
        

        return

    for paciente in lista_pacientes:
        indice = lista_pacientes.index(paciente) + 1 

        print(f"{indice}- Paciente: {paciente['nome_paciente']}, CPF: {paciente['cpf_paciente']}, Email: {paciente['email_paciente']}")


def excluir_paciente():
    listar_pacientes() #chama a função listar_pacientes para exibir os pacientes cadastrados no sistema, para que o usuario possa escolher qual paciente deseja excluir, o usuario vai ter que digitar o indice do paciente que deseja excluir

    try:
        paciente_exclude= int(input("Qual indice do paciente que deseja excluir:"))
        if paciente_exclude < 0 or paciente_exclude > len(lista_pacientes):
            
            print("Indice invalido")
            return 
        else:
            lista_pacientes.pop(paciente_exclude - 1)
            
            print("Paciente excluido com sucesso!")
            


    except ValueError:
        print("Digite apenas o indice, não o nome do paciente, ou qualquer outro cpf na lista")

# Função para verificar se o médico atingiu o limite de consultas
# feito em grupo na sala mas modificado por mim, tirando os list compression para melhor entendimento
def verificar_limite_consultas(medico_escolhido, dia_consulta):
    consultas_do_dia = [] #cria uma lista vazia para armazenar as consultas do dia
    for consulta in lista_consultas: #itera em cada consulta dentro da lista de consultas
        if consulta['medico_escolhido'] == medico_escolhido and consulta['dia_consulta'] == dia_consulta: #itera em toda a lista de consultas, olhando especificamente para o valor atribuido a "medico_escolhido" e "dia_consulta" para verificar se o medico ja atingiu o limite de consultas, se o for igual ao medico_escolhido e dia_consulta que esta sendo cadastrado, o medico ja atingiu o limite de consultas
            consultas_do_dia.append(consulta)

    # esse for fez o seguinte, ele ve se o medico escolhido é igual ao medico que esta na lista de consultas e se o dia da consulta é igual ao dia da consulta que esta na lista de consultas, se for, ele adiciona a consulta a lista consultas_do_dia
    #logo depois ele verifica se o tamanho da lista consultas_do_dia é menor que o limite de atendimentos do medico, se for, ele retorna True, se não, ele retorna False

    medico = None #Inicializa a variável medico com o valor None, o que significa que ainda não foi encontrado o médico correspondente.
    for med in lista_medicos: #Este laço percorre a lista de médicos registrados.
        if med['nome'] == medico_escolhido: #iVerifica se o nome do médico escolhido pelo usuário corresponde a algum dos médicos registrados.

            medico = med # Quando o nome do médico é encontrado, ele é atribuído à variável medico. Isso permite acessar os detalhes do médico, como o limite de consultas.
            break # Quando o médico é encontrado, o laço é interrompido.

    if medico and len(consultas_do_dia) <= medico['limite_atendimento']: #se o medico for diferente de None e o tamanho da lista consultas_do_dia for menor que o limite de atendimentos do medico, ele retorna True
        return True
    else:
        
        print("Médico atingiu o máximo de consultas!") #se o medico atingiu o limite de consultas, ele exibe a mensagem
        
        return False

# Função para agendar consulta
# feito em grupo na sala
def agendar_consulta():
    nome_paciente = input("Digite o nome do paciente: ").capitalize() #capitalize é um metodo que converte a primeira letra de uma string em maiúscula
    cpf_paciente = input("Digite o CPF do paciente (somentes numeros): ")

    # nova mudança: verificar se o paciente já está cadastrado 
    paciente_cadastrado = False
    for paciente in lista_pacientes:
        if paciente['cpf_paciente'] == cpf_paciente and paciente['nome_paciente'] == nome_paciente:
            paciente_cadastrado = True
            break

    if not paciente_cadastrado:
        print("Paciente não cadastrado no sistema!")
        print("Por favor, cadastre o paciente antes de agendar a consulta.")
        print("Redirecionando para o cadastro de paciente... Digite as credencias novamente")
        cadastrar_paciente()

    listar_medicos()

    medico_escolhido = input("Com que médico deseja se consultar: ")

    medico_existe = False # criamos uma variável para verificar se o médico escolhido existe, ela começa como False e posteriormente será alterada para True se o médico for encontrado
    for medico in lista_medicos: #itera em cada medico dentro da lista, ou seja percorremos a lista de medicos para verificar se o medico ja esta cadastrado
        if medico['nome'] == medico_escolhido: # verifica se o nome do medico é igual ao nome do medico que o usuário deseja pesquisar, se sim, ela exibe as informações do medico e altera a variável medico_encontrado para True
            medico_existe = True # se o medico escolhido existir, alteramos a variável medico_existe para True
            break

    if not medico_existe: #se o medico escolhido não existir, exibimos a mensagem de que o medico não foi encontrado, no caso se a varivael medico_existe for False
        print("Médico indisponível no consultório!")
        return

    dia_consulta = input("Qual o dia da consulta: ")

    if not verificar_limite_consultas(medico_escolhido, dia_consulta): #verifica se o médico atingiu o limite de consultas
        print("Este médico já atingiu o limite de consultas para o dia!")
        return
    else:
        

        hora_consulta = input("Qual o horário da consulta: ") 

        consulta = {
            'nome_paciente': nome_paciente,
            'cpf_paciente': cpf_paciente,
            'medico_escolhido': medico_escolhido,
            'dia_consulta': dia_consulta,
            'hora_consulta': hora_consulta
        }

        lista_consultas.append(consulta) #adiciona a consulta a lista de consultas
        print("Consulta agendada com sucesso!")

# Função para listar consultas
# feito por mim
def listar_consultas():
    print("Carregando consultas...")
    sleep(1)
    if not lista_consultas:
        print("Nenhuma consulta agendada!")
        return
    
    for consulta in lista_consultas:
        indice = lista_consultas.index(consulta) + 1 
        print(f"{indice}- Consulta agendada: Paciente {consulta['nome_paciente']} com o médico {consulta['medico_escolhido']} no dia {consulta['dia_consulta']} às {consulta['hora_consulta']}.")


def excluir_consulta():
    listar_consultas()
    try:
        consulta_exclude= int(input("Qual indice da consulta que deseja excluir:"))
        if consulta_exclude < 0 or consulta_exclude > len(lista_consultas): #verifica se o indice da consulta que o usuario deseja excluir é valido, valido seria entre 0 e o tamanho da lista de consultas
            print("Indice invalido")
            return 
        else:
            lista_consultas.pop(consulta_exclude - 1) #.pop é um metodo que remove o item de uma lista dado o seu indice, o indice é passado como argumento para o metodo .pop
            print("Consulta excluida com sucesso!")

    except ValueError:
        print("Digite apenas o indice, não o nome do paciente, ou qualquer outro cpf na lista")

def pesquisar_medico():
    nome_medico = input("Digite o nome do médico que deseja pesquisar: ").capitalize() #capitalize é um metodo que converte a primeira letra de uma string em maiúscula
    print("Procurando médico...")
    sleep(1)
    medico_encontrado = False # criamos uma variável para verificar se o médico foi encontrado, ela começa como False e posteriormente será alterada para True se o médico for encontrado
    for medico in lista_medicos: #itera em cada medico dentro da lista, ou seja percorremos a lista de medicos para verificar se o medico ja esta cadastrado
        if medico['nome'] == nome_medico: # verifica se o nome do medico é igual ao nome do medico que o usuário deseja pesquisar, se sim, ela exibe as informações do medico e altera a variável medico_encontrado para True
            print(f"Médico: {medico['nome']}, Especialidade: {medico['especialidade']}, Credencial: {medico['credencial']}, Limite de atendimentos: {medico['limite_atendimento']}")
            print("O médico atende nessa clínica")
            medico_encontrado = True 


            resposta = input('Deseja se consultar com esse médico? S/N').upper() #pedimos para o usuário digitar se deseja se consultar com o médico encontrado, o upper() é um método que converte a primeira letra de uma string em maiúscula
            if resposta == "S":
                agendar_consulta() # se a resposta for "S", chamamos a função agendar_consulta, voce vai ter que digitar as credenciais denovo, mas idai, é um sistema de ensino medio basico, eu poderia faazer melhor, mas eu nao quero
            else:
                print('Obrigado... Tchau!')
                break

    if not medico_encontrado: #se o medico especifio encontrado for False, ou seja, se o medico nao foi encontrado, exibimos a mensagem de que o medico nao foi encontrado
        print("Médico não encontrado!")

def pesquisar_paciente():
    nome_paciente = input("Digite o nome do paciente que deseja pesquisar: ").capitalize() #capitalize é um metodo que converte a primeira letra de uma string em maiúscula
    print("Procurando paciente...")
    sleep(1)
    paciente_encontrado = False
    for paciente in lista_pacientes:
        if paciente['nome_paciente'] == nome_paciente:
            print(f"Paciente: {paciente['nome_paciente']}, CPF: {paciente['cpf_paciente']}, Email: {paciente['email_paciente']}")
            print("O paciente está cadastrado no sistema")
            paciente_encontrado = True


            resposta = input('Deseja agendar uma consulta para esse paciente? S/N').capitalize()
            if resposta == "S":
                agendar_consulta()
            else:
                print('Obrigado... Tchau!')
                break

    if not paciente_encontrado:
        print("Paciente não encontrado!")

def pesquisar_consulta():
    cpf_paciente = input("Digite o CPF do paciente que marcou a consulta: ")
    print("Procurando consulta...")
    sleep(1)
    consulta_encontrada = False
    for consulta in lista_consultas:
        if consulta['cpf_paciente'] == cpf_paciente:
            print(f"Consulta: {consulta['nome_paciente']}, Médico: {consulta['medico_escolhido']}, Dia: {consulta['dia_consulta']}, Hora: {consulta['hora_consulta']}")
            print("A consulta está agendada")
            consulta_encontrada = True

            
            resposta = input('Deseja cancelar essa consulta? S/N').upper()
            if resposta == "S":
                excluir_consulta()
            else:
                print('Obrigado... Tchau!')
                break

    if not consulta_encontrada:
        print("Consulta não encontrada!")
