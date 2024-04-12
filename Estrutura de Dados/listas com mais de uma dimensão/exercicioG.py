import random

# Cria listas A e B com 7 elementos cada
a = [random.uniform(1, 10) for i in range(7)]
b = []
for linha in a :
    print("celsius: {:.2f}".format(linha))

for i in range(7):
    b.append((a[i]*1.8)+32)  # Fix the syntax error

# Imprime a matriz C
for linha in b:
    print("fahrenheint: {:.2f}".format(linha))
