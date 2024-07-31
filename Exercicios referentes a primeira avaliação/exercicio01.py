
# Faça um programa que calcule o fatorial de todos os numeros impares 
# dentre os 10 primeiros da sequência de Fibonacci. 

fibonacci = [1,1]
for i in range(2, 10):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(fibonacci[i])
for num in fibonacci:
    if num % 2 != 0:
        fatorial = 1
        for j in range(1, num+1):
            fatorial *= j
        print(fatorial)