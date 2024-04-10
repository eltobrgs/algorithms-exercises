
#bubblesort

a = [91,81,77,62,22,21,14,10,8,7,4]
print('Sem ordenaçao:', a)

for i in range (len(a)-1):
    for j in range (1+i, len(a)):
        if a[i]>a[j]:
            a[i], a[j]= a[j], a[i] 

print('Ordernado com bubble sort:', a)

inicio= 0
fim= len(a)-1
meio= (inicio+fim)//2
x=22
while inicio<=fim and a[meio]!=x:
    if x<a[meio]:
        fim= meio-1
    else:
        inicio= meio+1
    meio= (inicio+fim)//2
if a[meio]==x:
    print(f'Número {x} encontrado na posição {meio}')
else:
    print('Número não encontrado')
print('fim do programa')

'''
1-Ordenação Bubble Sort: A lista de números é definida na variável a. O código então imprime a lista antes da ordenação. 
O Bubble Sort começa com dois loops for aninhados que percorrem a lista. 
O loop interno compara cada elemento a[i] com o elemento seguinte a[j]. Se a[i] for maior que a[j], ele troca os dois elementos. 
Isso garante que o maior número se mova para o final da lista. O processo é repetido até que a lista esteja completamente ordenada. 
A lista ordenada é então impressa.

2-Busca Binária: A busca binária é um algoritmo eficiente para encontrar um item em uma lista ordenada. 
Ele começa definindo três variáveis: inicio, fim e meio, que representam o início, o fim e o meio da lista, respectivamente. 
O número que estamos procurando é definido na variável x. O código então entra em um loop while que continua enquanto inicio é menor ou igual 
a fim e o elemento do meio a[meio] é diferente de x. Se x for menor que o elemento do meio, 
o código redefine fim para ser meio - 1. Se x for maior, ele redefine inicio para ser meio + 1. 
O elemento do meio é então recalculado. Se o elemento do meio for igual a x, o código imprime a posição de x na lista. 
Se o loop terminar sem encontrar x, o código imprime que o número não foi encontrado.
'''
