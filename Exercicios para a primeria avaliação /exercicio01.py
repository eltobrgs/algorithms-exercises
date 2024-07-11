# Gerar os primeiros 10 números ímpares da sequência de Fibonacci
# Inicializar os primeiros dois termos
fib = [1, 1]

# Calcular os próximos termos
for i in range(2, 15):
    proxterm = fib[i-1] + fib[i-2]
    fib += [proxterm]

# Imprimir a série de Fibonacci até o décimo quinto termo
print(fib)
