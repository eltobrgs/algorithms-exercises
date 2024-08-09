# Função para verificar se um número é primo
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Teste para a função eh_primo
print(eh_primo(7))   # Resultado esperado: True
print(eh_primo(10))  # Resultado esperado: False
