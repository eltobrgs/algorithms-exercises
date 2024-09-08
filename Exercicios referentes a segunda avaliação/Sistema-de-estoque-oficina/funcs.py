'''Sistema que controla o estoque de uma casa de peças de automóveis (visão do vendedor).
- verificar se o CPF do comprador é válido 
- cadastrar o nome das peças e a quantidade de cada no estoque.
- em caso de compra de alguma peça diminuir no estoque'''



peças_em_estoque = []

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
    peça_adicionar= input("Digite o nome da peça: ")
    tipo_peça= input("Digite o tipo da peça: ")
    descricao_peça= input("Digite a descrição da peça: ")
    quantidade_adicionar= input("Digite a quantidade da peça: ")
    preço_peça= input("Digite o preço da peça: ")

    peça= {"nome": peça_adicionar,"descriçao da peça": descricao_peça ,"quantidade": quantidade_adicionar, "tipo": tipo_peça, "preço": preço_peça}
    peças_em_estoque.append(peça)
    print("Peça cadastrada no estoque da oficina com sucesso!")

def listar_peças():
    if len(peças_em_estoque) == 0:
        print("Nenhuma peça cadastrada no estoque.")
    else:
        print("Peças em estoque:")
        for peça in peças_em_estoque:
            indice = peças_em_estoque.index(peça)
            print(f"{indice + 1} - {peça['nome']} - {peça['tipo']} - {peça['descriçao da peça']} - {peça['quantidade']}- {peça['preço']}")


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
        if int(peça["quantidade"]) >= quantidade_vendida:
            peça["quantidade"] = int(peça["quantidade"]) - quantidade_vendida
            preço_total = quantidade_vendida * float(peça["preço"])
            print(f"Venda realizada com sucesso para o cliente {cliente}!")
            print(f"Quantidade restante no estoque: {peça['quantidade']}")
            print(f"Preço total: R${preço_total}")


            
            print('nota fiscal:')
            print(f"Cliente: {cliente}")
            print(f"CPF: {cpf_cliente}")
            print(f"Peça: {peça['nome']}")
            print(f"Tipo: {peça['tipo']}")
            print(f"Descrição: {peça['descriçao da peça']}")
            print(f"Quantidade vendida: {quantidade_vendida}")
            print(f"Preço unitário: R${peça['preço']}")
            print(f"Preço total: R${preço_total}")
        else:
            print("Quantidade insuficiente no estoque.")
            print(f"Nos temos apenas {peça['quantidade']} no estoque.")




def menu():
    print("1 - Cadastrar peça")
    print("2 - Listar peças")
    print("3 - Vender peça")
    print("4 - Sair")
    opcao = input("Digite a opção desejada: ")
    return opcao

