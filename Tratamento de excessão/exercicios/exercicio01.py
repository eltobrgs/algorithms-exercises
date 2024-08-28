import time

# Função iterativa para calcular o n-ésimo número de Fibonacci
def fibonacci_iterativa(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci_recursiva(n):
    if n <= 1:
        return n
    return fibonacci_recursiva(n - 1) + fibonacci_recursiva(n - 2)

# Função para calcular o tempo de execução de uma função
def calcular_tempo(func, n):
    comeco = time.time()
    func(n)
    return time.time() - comeco

# Função principal
def main():
    try:
        n = 10  # Número de Fibonacci a ser calculado (pode ser ajustado)

        # Calculando e medindo o tempo da função iterativa
        tempo_iterativo = calcular_tempo(fibonacci_iterativa, n)
        print(f"Tempo de execução da função iterativa: {tempo_iterativo:.6f} segundos")

        # Calculando e medindo o tempo da função recursiva (com um número pequeno)
        tempo_recursivo = calcular_tempo(fibonacci_recursiva, n)
        print(f"Tempo de execução da função recursiva: {tempo_recursivo:.6f} segundos")

        # Comparando qual foi mais rápida
        if tempo_iterativo < tempo_recursivo:
            print("A função iterativa foi mais rápida.")
        else:
            print("A função recursiva foi mais rápida.")
    
    except RecursionError:
        print("A função recursiva não conseguiu calcular o número de Fibonacci devido a um erro de recursão.")
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
    finally:
        print("Fim do programa.")

# Executar o programa
if __name__ == "__main__":
    main()
