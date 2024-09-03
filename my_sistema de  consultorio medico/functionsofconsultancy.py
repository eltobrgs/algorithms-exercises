# Função para validar CPF
def cpfvalido(cpf):
    # Verifica se o CPF tem 11 dígitos e é numérico
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Converte o CPF em uma lista de inteiros
    cpf = [int(digit) for digit in cpf]

    # Calcula o primeiro dígito verificador
    soma1 = sum(cpf[i] * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma2 = sum(cpf[i] * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    # Verifica se os dígitos calculados correspondem aos dígitos fornecidos
    return digito1 == cpf[9] and digito2 == cpf[10]

# Função para cadastrar um médico
def cadastrar_medico(medicos):
    nome = input("Digite o nome do médico: ")
    especialidade = input("Digite a especialidade do médico: ")

    # Verifica se o médico já foi cadastrado
    if nome in medicos:
        print("Médico já cadastrado.")
    else:
        medico = {"nome": nome, "especialidade": especialidade}
        medicos[nome] = medico
        print("Médico cadastrado com sucesso!")

# Função para cadastrar um paciente
def cadastrar_paciente(pacientes):
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o CPF do paciente (11 dígitos): ")

    # Valida o CPF
    if cpfvalido(cpf):
        telefone = input("Digite o telefone do paciente: ")
        email = input("Digite o e-mail do paciente: ")

        paciente = {"nome": nome, "cpf": cpf, "telefone": telefone, "email": email}
        pacientes[cpf] = paciente
        print("Paciente cadastrado com sucesso!")
    else:
        print("CPF inválido. Tente novamente.")

# Função para agendar uma consulta
def agendar_consulta(medicos, pacientes, consultas):
    if not medicos:
        print("Nenhum médico cadastrado.")
        return
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    cpf_paciente = input("Digite o CPF do paciente para agendar a consulta: ")
    if cpf_paciente in pacientes:
        paciente = pacientes[cpf_paciente]
    else:
        print("Paciente não encontrado.")
        return

    nome_medico = input("Digite o nome do médico para agendar a consulta: ")
    if nome_medico in medicos:
        medico = medicos[nome_medico]
    else:
        print("Médico não encontrado.")
        return

    consulta = {"paciente": paciente, "medico": medico}
    consultas.append(consulta)
    print("Consulta agendada com sucesso!")

# Função para listar consultas
def listar_consultas(consultas):
    if consultas:
        print("Consultas agendadas:")
        for consulta in consultas:
            print(f"Paciente: {consulta['paciente']['nome']} - Médico: {consulta['medico']['nome']} ({consulta['medico']['especialidade']})")
    else:
        print("Nenhuma consulta agendada.")

# Função para excluir uma consulta
def excluir_consulta(consultas):
    if consultas:
        print("Consultas agendadas:")
        for i, consulta in enumerate(consultas):
            print(f"{i + 1} - Paciente: {consulta['paciente']['nome']} - Médico: {consulta['medico']['nome']} ({consulta['medico']['especialidade']})")
        
        consulta_idx = int(input("Digite o número da consulta a ser excluída: ")) - 1
        if 0 <= consulta_idx < len(consultas):
            consultas.pop(consulta_idx)
            print("Consulta excluída com sucesso!")
        else:
            print("Consulta selecionada inválida.")
    else:
        print("Nenhuma consulta agendada.")

