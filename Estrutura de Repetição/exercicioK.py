#calcula a somatoria dos grãos de trigo de um tabuleiro de xadres com while
cont=1
soma=0
while cont<=64:
    soma=(2**cont)-1
    print(soma)
    cont+=1
print(") total de grãos de trigo é ", soma)