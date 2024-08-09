# Função para verificar se um número é ímpar
def eh_impar(numero):
    if numero % 2 != 0:
        return True
    else:
        return False

# Teste para a função eh_impar
print(eh_impar(4))  # Resultado esperado: False
print(eh_impar(7))  # Resultado esperado: True