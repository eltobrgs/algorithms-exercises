# Função para calcular o fatorial de um número
def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result