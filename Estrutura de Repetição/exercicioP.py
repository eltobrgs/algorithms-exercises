'''#programa que imprime a soma da media aritmetica dos valores de 50 a 70 com for
soma=0
for i in range(50,71):
    soma+=i
media=soma/20
print("A soma dos valores de 50 a 70 é: ", soma)
print("A média aritmética dos valores de 50 a 70 é: ", media)'''

 #programa que imprime a soma da media aritmetica dos valores de 50 a 70 com while 
cont=50
soma=0
while cont<=70:
    soma+=cont
    cont+=1
media=soma/20
print("A soma dos valores de 50 a 70 é: ", soma)
print("A média aritmética dos valores de 50 a 70 é: ", media)