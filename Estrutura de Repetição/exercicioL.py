#soamtorio fatorial de 15 numeros com for
soma=0
for i in range(1,16):
    fatorial=1
    for j in range(1,i):
        fatorial*=j
    soma*=fatorial
print("O somatório dos fatoriais de 1 a 15 é: ", soma)