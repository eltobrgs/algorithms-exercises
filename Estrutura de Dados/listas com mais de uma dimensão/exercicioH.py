import random

# Cria listas A e B com 7 elementos cada
a = [[random.randint(1, 10) for i in range(3)] for j in range(3)]
b = []

# Combina os elementos das listas A e B em uma matriz C
for i in range(3):
    
    for j in range(3):
        if i==j:
            b.append(3* a[i][j])
            
        else:
            b.append(2* a[i][j])
            

# Imprime a matriz b
for linha in a:
    print(linha)
print(b)