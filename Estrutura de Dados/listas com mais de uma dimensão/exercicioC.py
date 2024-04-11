import random
a = [[random.randint(0, 9) for i in range(3)] for j in range(5)]
print(a)
for linha in a:
    print(linha)