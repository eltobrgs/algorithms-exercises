
def calcular_fibonacci(n):
    fibonacci = [0, 1]  # Inicializa a sequência com os dois primeiros números
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])  # Calcula o próximo número da sequência
    return fibonacci

# Teste para a função calcular_fibonacci
print(calcular_fibonacci(5))   # Resultado esperado: [0, 1, 1, 2, 3]
print(calcular_fibonacci(10))  # Resultado esperado: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]