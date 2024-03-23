'''fatorial=1
contador=1
while contador <= 5:
    fatorial *= contador
    contador += 1
print(fatorial)'''

'''fatorial=1
for contador in range(1, 6):
    fatorial *= contador
print(fatorial)'''

resposta= "S"
while resposta == "S":
    resposta = input("Deseja continuar? (S/N) ").upper()
    if resposta=="S":
        num=int(input('digite um numero qualquer:'))
        fatorial=1
        for contador in range(1, num+1):
            fatorial *= contador
        print(fatorial)
    elif resposta=="N":
        print('Fim do programa')
    else:
        print('Resposta invalida')
        resposta = "S"
