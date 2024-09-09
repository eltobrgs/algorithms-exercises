peças_em_estoque = [
    {"nome": "Pneu", "descriçao da peça": "Pneu 185/65 R15", "quantidade": 10, "tipo": "Rodagem", "preço": 250.00},
    {"nome": "Bateria", "descriçao da peça": "Bateria 60Ah", "quantidade": 5, "tipo": "Elétrica", "preço": 350.00},
    {"nome": "Filtro de Óleo", "descriçao da peça": "Filtro de óleo para motor 1.6", "quantidade": 20, "tipo": "Motor", "preço": 40.00},
    {"nome": "Pastilha de Freio", "descriçao da peça": "Pastilha de freio dianteira", "quantidade": 15, "tipo": "Freios", "preço": 150.00}
]
# iniciando o estoque com algumas peças para teste

# essa funçao verifica se o cpf é válido
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

# funçao para cadastrar peças
def cadastrar_peça():
    peça_adicionar = input("Digite o nome da peça: ")
    tipo_peça = input("Digite o tipo da peça: ")
    descricao_peça = input("Digite a descrição da peça: ")
    quantidade_adicionar = int(input("Digite a quantidade da peça: "))
    preço_peça = float(input("Digite o preço da peça: "))
    # pedimos para o usuário digitar o nome, tipo, descrição e quantidade da peça para poder adicionar ao estoque
    # nos pedimos para o usuário digitar o preço da peça como float, para que ele possa digitar valores decimais

    
    # criamos um dicionário com as informações da peça e adicionamos ao estoque
    peça = {"nome": peça_adicionar, "descriçao da peça": descricao_peça, "quantidade": quantidade_adicionar, "tipo": tipo_peça, "preço": preço_peça}
    peças_em_estoque.append(peça)
    # usamos o método append para adicionar a peça ao estoque
    print("Peça cadastrada no estoque da oficina com sucesso!")

def listar_peças():
    # se a quatiade de peças no estoque for igual a 0, exibimos a mensagem
    if len(peças_em_estoque) == 0:
        print("Nenhuma peça cadastrada no estoque.")
    else:
        print("Peças em estoque:")
         # se houver peças no estoque, exibimos as informações delas com um loop iterando sobre a lista de peças, ou seja, para cada peça na lista de peças, exibimos as informações dela
        for indice, peça in enumerate(peças_em_estoque, start=1):
            # usamos o método enumerate para obter o índice da peça na lista e exibimos as informações da peça, usamos o start=1 para começar a contagem do índice em 1
            print(f"{indice} - {peça['nome']} - {peça['tipo']} - {peça['descriçao da peça']} - Quantidade: {peça['quantidade']} - Preço: R${peça['preço']:.2f}")


def pesquisar_peça(): 
    # pedimos para o usuário digitar o nome da peça que deseja pesquisar
    peça_pesquisar = input("Digite o nome da peça que deseja pesquisar: ")
    print("Procurando peça...")
    peça_encontrada = False # criamos uma variável para verificar se a peça foi encontrada, ela começa como False e posteriormente será alterada para True se a peça for encontrada
    for peça in peças_em_estoque: #itera em cada peça dentro do estoque
        if peça['nome'] == peça_pesquisar: # verifica se o nome da peça é igual ao nome da peça que o usuário deseja pesquisar, se sim, ela exibe as informações da peça e altera a variável peça_encontrada para True
            print(f"Peça encontrada: {peça['nome']} - {peça['tipo']} - {peça['descriçao da peça']} - Quantidade: {peça['quantidade']} - Preço: R${peça['preço']:.2f}")
            peça_encontrada = True
            break

    if not peça_encontrada: # se a peça não for encontrada, a variel peça_encontrada continuará como False e exibiremos a mensagem de que a peça não foi encontrada
        print("Peça não encontrada!")


# funçao para vender peças
def vender_peça():
    # chamamos a funçao de listar peças para exibir as peças disponíveis no estoque
    listar_peças()
    cliente = input("Digite o nome do cliente: ")
    cpf_cliente = input("Digite o CPF do cliente: ")
    # pedimos para o usuário digitar o nome e o cpf do cliente para realizar a venda
    # chamamos a funçao de verificar se o cpf é válido

    # se o cpf for inválido, exibimos a mensagem e retornamos da funçao
    if cpf_valido(cpf_cliente) == "CPF inválido.":
        print("CPF inválido.")
        return
    else:
        # se o cfp for valido perguntamos qual peça o cliente deseja comprar e a quantidade
        peça_vendida = int(input("Digite o número da peça que deseja vender: "))
        quantidade_vendida = int(input("Digite a quantidade que deseja vender: "))
        peça = peças_em_estoque[peça_vendida - 1]   
        # subtraímos 1 do número da peça para obter o índice correto da peça na lista de peças    
        # se nao fizéssemos isso, o índice da peça seria o número da peça - 1, pois a lista começa com o índice 0    
        
        if peça["quantidade"] >= quantidade_vendida:
        # verificamos se a quantidade da peça no estoque é maior ou igual a quantidade que o cliente deseja comprar
            # se for, subtraímos a quantidade vendida da quantidade da peça no estoque
            peça["quantidade"] -= quantidade_vendida
            # calculamos o preço total da venda
            preço_total = quantidade_vendida * peça["preço"]

            # depois de realizar a venda, exibimos as informações da venda e a nota fiscal
            print(f"Venda realizada com sucesso para o cliente {cliente}!")
            print(f"Quantidade restante no estoque: {peça['quantidade']}")
            print(f"Preço total: R${preço_total:.2f}") # esse :.2f formata o número para ter apenas 2 casas decimais após a vírgula

            print("-" * 30)
            print('Nota fiscal:')
            print(f"Cliente: {cliente}")
            print(f"CPF: {cpf_cliente}")
            print(f"Peça: {peça['nome']}")
            print(f"Tipo: {peça['tipo']}")
            print(f"Descrição: {peça['descriçao da peça']}")
            print(f"Quantidade vendida: {quantidade_vendida}")
            print(f"Preço unitário: R${peça['preço']:.2f}")
            print(f"Preço total: R${preço_total:.2f}") 
            print("-" * 30)
        else:
            print("Quantidade insuficiente no estoque.")
            print(f"Temos apenas {peça['quantidade']} unidades no estoque.")



