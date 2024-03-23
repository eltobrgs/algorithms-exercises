#programa que imprime o total do somatório, medias e total dos números 
#lidos ate que seja um numero negativo
soma=0
cont=1
while True:
    num=int(input("Digite um numero: "))
    if num<0: 
        break
    soma+=num
    media=soma/cont
    cont+=1
print("Total do somatório: ", soma)
print("Media: ", media)
print("Total de números lidos: ", cont-1)