# Função para calcular a soma de números em uma lista
def calcular_soma(numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma

# Teste para a função calcular_soma
print(calcular_soma([1, 2, 3, 4]))  # Resultado esperado: 10
print(calcular_soma([10, 20, 30]))  # Resultado esperado: 60
