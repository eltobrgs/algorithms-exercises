import random

#bubblesort
a = [random.randint(0,100) for i in range(10)]

for i in range (len(a)-1):
    for j in range (1+i, len(a)):
        if a[i]>a[j]:
            a[i], a[j]= a[j], a[i]
            
print(a)

'''O código fornecido implementa o algoritmo de ordenação Bubble Sort. Vou explicar passo a passo o que está acontecendo no código:

1. Primeiro, o módulo `random` é importado para gerar números aleatórios.
2. Em seguida, é criada uma lista chamada `a` que contém 10 números inteiros aleatórios no intervalo de 0 a 100. 
Isso é feito usando uma compreensão de lista e a função `randint` do módulo `random`.
3. O algoritmo Bubble Sort é implementado usando dois loops `for`. O primeiro loop `for` itera sobre os elementos da lista `a`, 
exceto o último elemento. Isso é feito usando a função `len(a)-1` como o limite superior do loop.
4. Dentro do primeiro loop `for`, há um segundo loop `for` que itera sobre os elementos da lista `a` a partir do índice `1+i` 
até o final da lista. Isso é feito usando a função `range(1+i, len(a))`.
5. Dentro do segundo loop `for`, há uma condição `if` que verifica se o elemento atual `a[i]` é maior do que o próximo elemento `a[j]`.
 Se essa condição for verdadeira, os elementos são trocados de posição usando a sintaxe `a[i], a[j] = a[j], a[i]`. 
 Isso garante que os elementos maiores sejam movidos para o final da lista.
6. Após a conclusão dos loops `for`, a lista `a` está ordenada em ordem crescente.
7. Por fim, a lista ordenada é impressa na saída usando a função `print(a)`.

O Bubble Sort é um algoritmo de ordenação simples, mas não é eficiente para grandes conjuntos de dados, 
pois requer várias iterações e trocas de elementos. No entanto, é útil para fins educacionais e para pequenos conjuntos de dados.'''