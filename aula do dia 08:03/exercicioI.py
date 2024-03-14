#usando for ao invés de while
# Inicializar os primeiros dois termos
fib = [1, 1]

# Calcular os próximos termos
for i in range(2, 15):
    proxterm = fib[i-1] + fib[i-2]
    fib += [proxterm]

# Imprimir a série de Fibonacci até o décimo quinto termo
print(fib)

# Inicializar os primeiros dois termos
fib = [1, 1]

# Calcular os próximos termos usando for
'''
# Calcular os próximos termos usando while
i = 2
while i < :
    proxterm = fib[i-1] + fib[i-2]

    fib += [proxterm]
    i += 1

# Imprimir a série de Fibonacci até o décimo quinto termo
print(fib)'''

