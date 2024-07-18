# Pergunta o CPF ao usuário
cpf = input("Digite o CPF (somente números): ")

# Verifica se o CPF tem 11 dígitos
if len(cpf) != 11 or not cpf.isdigit():#o isdigit() verifica se a string é composta apenas por números
                                        #se for composta apenas por números, ele retorna True, caso contrário, retorna False. 
                                        #ele é uma função de string do python, mas nao é nesseria para o codigo, botei pra deixar mais clean e seguro
    print("CPF inválido.")
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
            print("CPF válido.")
        else:
            print("CPF inválido.")
    else:
        print("CPF inválido.")
