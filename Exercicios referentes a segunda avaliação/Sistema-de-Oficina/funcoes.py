# Função para verificar se um CPF é válido
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


# Lista para armazenar os clientes
lista_clientes = []

# Lista para armazenar os carros na oficina
carros_na_oficina = []

# Lista para armazenar os serviços realizados
servicos = []


# Função para cadastrar um cliente
def cadastrar_cliente():
    nome = input('Digite o nome do cliente: ').capitalize() # usamos o método capitalize para garantir que o nome do cliente seja exibido com a primeira letra em maiúsculo
    email = input('Digite o email do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    cpf = input('Digite o cpf do cliente: ')

    # Verifica se o CPF é válido
    if cpf_valido(cpf) == 'CPF inválido.':
        print('CPF inválido.')
        return
    else:
        # Cria um dicionário com os dados do cliente e adiciona à lista de clientes
        cliente = {'nome': nome, 'email': email, 'telefone': telefone, 'cpf': cpf}
        # usa o método append para adicionar o dicionario que contem as informaçoes do cliente à lista de clientes
        lista_clientes.append(cliente)
        print('Cliente cadastrado com sucesso!')


# Função para listar os clientes cadastrados
def listar_clientes():
    # se a quantidade de clientes na lista for igual a 0, exibimos a mensagem
    if len(lista_clientes) == 0:
        print('Nenhum cliente cadastrado!')
        return
    # se houver clientes na lista, exibimos as informações deles com um loop iterando sobre a lista de clientes, ou seja, para cada cliente na lista de clientes, exibimos as informações dele
    else:
        print('Listando clientes...')
        # Enumera os clientes e exibe suas informações
        for indice, cliente in enumerate(lista_clientes, start=1): 
            # usamos o método enumerate para obter o índice do cliente na lista e exibimos as informações do cliente, usamos o start=1 para começar a contagem do índice em 1
            print(f" {indice}- Cliente: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}, CPF: {cliente['cpf']}")


# Função para excluir um cliente
def excluir_cliente():
    if len(lista_clientes) == 0:
        print('Nenhum cliente cadastrado!')
        return
    else:
        # Lista os clientes cadastrados
        listar_clientes()
        cliente_exclude = int(input('Digite o índice do cliente que deseja excluir: '))
        if 0 < cliente_exclude <= len(lista_clientes):# se o índice fornecido for válido, excluímos o cliente da lista de clientes, funciona da mesma forma que a funçao de excluir peças
            # Remove o cliente da lista de clientes
            lista_clientes.pop(cliente_exclude - 1)
            # usa o método pop para remover o cliente da lista de clientes, subtraímos 1 do índice fornecido para obter o índice correto do cliente na lista de clientes
            print('Cliente excluído com sucesso!')
        else:
            print('Índice inválido!')

def excluir_carro(): 
    if len(carros_na_oficina) == 0:
        print('Nenhum carro cadastrado!')
        return
    else:
        listar_carros()
        carro_exclude = int(input('Digite o índice do carro que deseja excluir: '))
        if 0 < carro_exclude <= len(carros_na_oficina):
            carros_na_oficina.pop(carro_exclude - 1)
            print('Carro excluído com sucesso!')
        else:
            print('Índice inválido!')

# Função para cadastrar um carro na oficina
def cadastrar_carro():
    placa = input('Digite a placa do carro: ')
    modelo = input('Digite o modelo do carro: ')
    ano = input('Digite o ano do carro: ')
    cor = input('Digite a cor do carro: ')
    nome_cliente = input('Digite o nome do cliente: ').capitalize()

    descricao = input('Digite a descrição do problema: ')
    servico = input('Digite o serviço a ser realizado: ')
    preco = int(input('Digite o preço do serviço (Após avaliação do mecânico): '))

    cliente_encontrado = False  # Variável para verificar se o cliente foi encontrado, partimos de uma premissa falsa
    for cliente in lista_clientes:
        if cliente['nome'] == nome_cliente: # Se o nome do cliente for igual ao nome fornecido, o cliente foi encontrado e a variável cliente_encontrado é alterada para True
            cliente_encontrado = True
            print('Cliente encontrado!')
            break
        
    if not cliente_encontrado: # Se a variável cliente_encontrado for False, exibimos a mensagem de que o cliente não foi encontrado
        print('Cliente não encontrado!')
        return
    else:
        # Cria um dicionário com os dados do carro e adiciona à lista de carros na oficina
        carro = {
            'placa': placa,
            'modelo': modelo,
            'ano': ano,
            'cor': cor,
            'cliente': nome_cliente,
            'descricao': descricao,
            'servico': servico,
            'preço do serviço': preco
        }
        # usa o método append para adicionar o dicionario que contem as informaçoes do carro à lista de carros na oficina
        carros_na_oficina.append(carro)
        print('Carro cadastrado com sucesso!')


# Função para listar os carros na oficina
def listar_carros():
    if len(carros_na_oficina) == 0:
        print('Nenhum carro cadastrado!')
        return
    else:
        print('Listando carros...')
        # Enumera os carros e exibe suas informações
        for indice, carro in enumerate(carros_na_oficina, start=1):
            print(f" {indice}- Carro: {carro['modelo']}, Placa: {carro['placa']}, Ano: {carro['ano']}, Cor: {carro['cor']}, Cliente: {carro['cliente']}, Descrição: {carro['descricao']}")


# Função para gerar o relatório de um carro
# Função para gerar o relatório de um carro
def relatorio():
    if len(carros_na_oficina) == 0:
        print('Nenhum carro cadastrado!')
        return
    else:
    
        # Solicita ao usuário o índice do carro que deseja ver o relatório
        print('De qual carro deseja ver o relatório?')
        listar_carros()
        carro_indice = int(input('Digite o índice do carro que deseja ver o relatório: '))

        # Verifica se o índice fornecido é válido
        if 0 < carro_indice <= len(carros_na_oficina):
            # Obtém o carro correspondente ao índice fornecido
            carro = carros_na_oficina[carro_indice - 1]

            # Exibe as informações do carro e do serviço realizado
            print(f"Carro: {carro['modelo']}, Placa: {carro['placa']}, Ano: {carro['ano']}, Cor: {carro['cor']}, Cliente: {carro['cliente']}, Descrição: {carro['descricao']}, Serviço: {carro['servico']}, Preço do serviço: {carro['preço do serviço']}")
            print('Relatório gerado com sucesso!')

            # Remove o carro da lista de carros na oficina
            carros_na_oficina.pop(carro_indice - 1)
            print('Serviço concluído, excluindo carro do sistema!')
        else:
            print('Índice inválido!')
