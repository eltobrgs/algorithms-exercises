# Pergunta o CPF ao usuário
cpf = input("Digite o CPF (somente números): ")

# Verifica se o CPF tem 11 dígitos
if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido.")
else:
    # Converte o CPF em uma lista de inteiros
    cpf = [int(digit) for digit in cpf]

    # Calcula o primeiro dígito verificador
    soma1 = sum(cpf[i] * (10 - i) for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    # Calcula o segundo dígito verificador
    soma2 = sum(cpf[i] * (11 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    # Verifica se os dígitos calculados são iguais aos fornecidos
    if digito1 == cpf[9] and digito2 == cpf[10]:
        print("CPF válido.")
    else:
        print("CPF inválido.")
