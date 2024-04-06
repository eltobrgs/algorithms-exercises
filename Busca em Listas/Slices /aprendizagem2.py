a = [5, 3, 8, 1, 9, 2, 7, 4, 6, 10, 14, 11, 13, 12, 15]

menor = a[0]
maior = a[0]

for i in a:
    if i < menor:
        menor = i
    if i > maior: # neste caso pode ser usado um else em vez de if
        maior = i

print('Menor elemento:', menor)
print('Maior elemento:', maior)