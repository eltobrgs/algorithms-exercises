import random

# Cria listas A e B com 7 elementos cada
a = [random.randint(1, 10) for i in range(7)]
b = [random.randint(1, 10) for i in range(7)]
c = []
print("A:", a)
print("B:", b)

# Combina os elementos das listas A e B em uma matriz C
for i in range(7):
    c.append([a[i], b[i]])

# Imprime a matriz C
for linha in c:
    print(linha)