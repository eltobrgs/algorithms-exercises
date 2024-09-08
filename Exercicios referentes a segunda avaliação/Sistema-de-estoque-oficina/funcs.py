peças_em_estoque = [
    {"nome": "Pneu", "descriçao da peça": "Pneu 185/65 R15", "quantidade": 10, "tipo": "Rodagem", "preço": 250.00},
    {"nome": "Bateria", "descriçao da peça": "Bateria 60Ah", "quantidade": 5, "tipo": "Elétrica", "preço": 350.00},
    {"nome": "Filtro de Óleo", "descriçao da peça": "Filtro de óleo para motor 1.6", "quantidade": 20, "tipo": "Motor", "preço": 40.00},
    {"nome": "Pastilha de Freio", "descriçao da peça": "Pastilha de freio dianteira", "quantidade": 15, "tipo": "Freios", "preço": 150.00}
]

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
        
def cadastrar_peça():
    peça_adicionar = input("Digite o nome da peça: ")
    tipo_peça = input("Digite o tipo da peça: ")
    descricao_peça = input("Digite a descrição da peça: ")
    quantidade_adicionar = int(input("Digite a quantidade da peça: "))
    preço_peça = float(input("Digite o preço da peça: "))

    peça = {"nome": peça_adicionar, "descriçao da peça": descricao_peça, "quantidade": quantidade_adicionar, "tipo": tipo_peça, "preço": preço_peça}
    peças_em_estoque.append(peça)
    print("Peça cadastrada no estoque da oficina com sucesso!")

def listar_peças():
    if len(peças_em_estoque) == 0:
        print("Nenhuma peça cadastrada no estoque.")
    else:
        print("Peças em estoque:")
        for indice, peça in enumerate(peças_em_estoque, start=1):
            print(f"{indice} - {peça['nome']} - {peça['tipo']} - {peça['descriçao da peça']} - Quantidade: {peça['quantidade']} - Preço: R${peça['preço']:.2f}")

def vender_peça():
    listar_peças()
    cliente = input("Digite o nome do cliente: ")
    cpf_cliente = input("Digite o CPF do cliente: ")
    if cpf_valido(cpf_cliente) == "CPF inválido.":
        print("CPF inválido.")
        return
    else:
        peça_vendida = int(input("Digite o número da peça que deseja vender: "))
        quantidade_vendida = int(input("Digite a quantidade que deseja vender: "))
        peça = peças_em_estoque[peça_vendida - 1]
        
        if peça["quantidade"] >= quantidade_vendida:
            peça["quantidade"] -= quantidade_vendida
            preço_total = quantidade_vendida * peça["preço"]
            print(f"Venda realizada com sucesso para o cliente {cliente}!")
            print(f"Quantidade restante no estoque: {peça['quantidade']}")
            print(f"Preço total: R${preço_total:.2f}")

            print('Nota fiscal:')
            print(f"Cliente: {cliente}")
            print(f"CPF: {cpf_cliente}")
            print(f"Peça: {peça['nome']}")
            print(f"Tipo: {peça['tipo']}")
            print(f"Descrição: {peça['descriçao da peça']}")
            print(f"Quantidade vendida: {quantidade_vendida}")
            print(f"Preço unitário: R${peça['preço']:.2f}")
            print(f"Preço total: R${preço_total:.2f}")
        else:
            print("Quantidade insuficiente no estoque.")
            print(f"Temos apenas {peça['quantidade']} unidades no estoque.")



