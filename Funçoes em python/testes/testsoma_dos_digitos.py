# Função para calcular a soma dos dígitos de um número
def soma_dos_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

# Teste para a função soma_dos_digitos
print(soma_dos_digitos(1234))  # Resultado esperado: 10
print(soma_dos_digitos(5678))  # Resultado esperado: 26
