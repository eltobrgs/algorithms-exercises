# Função para verificar se um número é par
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Teste para a função eh_par
print(eh_par(4))  # Resultado esperado: True
print(eh_par(7))  # Resultado esperado: False
