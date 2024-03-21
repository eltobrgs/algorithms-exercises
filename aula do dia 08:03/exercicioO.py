'''#programa que imprime o fatorial dos numeros impares de 1 a 10 com for 
for i in range(1,11,2):
    fatorial=1
    for j in range(1,i+1):
        fatorial*=j
    print(fatorial)'''

#programa que imprime o fatorial dos numeros impares de 1 a 10
cont=1
while cont<=10:
    if cont%2!=0:
        fatorial=1
        cont2=1
        while cont2<=cont:
            fatorial*=cont2
            cont2+=1
        print(fatorial)
    cont+cont+1