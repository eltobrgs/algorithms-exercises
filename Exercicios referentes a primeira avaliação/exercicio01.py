
# Faça um programa que calcule o fatorial de todos os numeros impares 
# dentre os 10 primeiros da sequência de Fibonacci. 

fibonacci=(1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
for i in fibonacci:
    if i%2!=0:
        fatorial=1
        for j in range(1,i+1):
            fatorial*=j
        print(fatorial)

        