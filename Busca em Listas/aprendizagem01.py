#meu jeito


l = [1,2,3,4,5,6,7,8,9,10]

while True:
    n = int(input("Digite um número inteiro: "))
    if n in l:
        print(f"Número {n} existe na lista")
        next= str(input("Deseja continuar? sim ou não: "))
        if next== "nao":
            break
    else:
        print(f"Número {n} não existe na lista")
        resp = str(input("Deseja adicionar um número na lista? sim ou não: ")) 
        if resp == "sim":
            l.append(n)
            print(f"Lista atualizada: {l}")
            next= str(input("Deseja continuar? sim ou não: "))
            if next== "nao":
                break
        else:
            print('ok')
            break
        
'''
#jeito do professor (SEM O 'IN')
l=[1,2,3,4,5,6,7,8,9,10]
resp='sim'
while True:
    achou=False
    n=int (input('Digite um número inteiro: '))
    cont=0
    while cont<len(l):
        if l[cont]==n:
            achou=True
            break
        cont+=1
    if achou:
        print(f'Número {n} existe na lista, na posiçao {cont+1}')
    else:
        print(f'Número {n} não existe na lista')
        resp=input('Deseja adicionar um número na lista? sim ou não: ')
        if resp=='sim':
            l.append(n)
            print(f'Lista atualizada: {l}')
        else:
            print('ok')
            break'''