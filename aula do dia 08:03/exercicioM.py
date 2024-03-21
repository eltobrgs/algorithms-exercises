'''#programa que lê dez valores e apresenta a soma desses valores e a media deles 
soma=0
for i in range(1,11):
    valor=int(input("Digite o valor: "))
    soma+=valor
media=soma/10
print("A soma dos valores é: ", soma)
print("A media dos valores é: ", media)'''

#programa que lê dez valores e apresenta a soma desses valores e a media deles 
soma=0
cont=1
while cont<=10:
    valor=int(input("Digite o valor: "))
    soma+=valor
    cont+=1
media=soma/10
print("A soma dos valores é: ", soma)
print("A media dos valores é: ", media)