# Função para calcular o fatorial de um número
def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Teste para a função fatorial
print(fatorial(5))  # Resultado esperado: 120
print(fatorial(0))  # Resultado esperado: 1
