'''
Bubble Sort é um algoritmo de classificação simples que funciona repetidamente percorrendo a lista a ser classificada, 
comparando cada par de itens adjacentes e trocando-os se estiverem na ordem errada. O passe pela lista é repetido até que a lista seja classificada.

Aqui está um exemplo passo a passo de como o Bubble Sort funciona:

Suponha que temos a seguinte lista de números: [5, 3, 8, 4, 2]

1. Começamos comparando os dois primeiros números (5 e 3). Como 5 é maior que 3 e queremos ordenar a lista em ordem crescente, trocamos os números. 
A lista agora se parece com isso: [3, 5, 8, 4, 2]
2. Em seguida, comparamos os próximos dois números (5 e 8). Como 5 é menor que 8, deixamos os números como estão.
3. Continuamos esse processo para o resto da lista. Quando chegamos ao final da lista, começamos novamente desde o início.
4. Continuamos esse processo até que possamos percorrer toda a lista sem ter que trocar nenhum número. Isso significa que a lista está ordenada.

Aqui está um exemplo de código Python para o Bubble Sort:



Este código define uma função `bubble_sort` que aceita uma lista de números como entrada e retorna a lista ordenada. 
A função usa um loop `for` para percorrer cada elemento da lista. Se o elemento atual for maior que o próximo, ele troca os dois elementos. 
Se nenhum elemento foi trocado na última passagem, a função sabe que a lista está ordenada e termina o processo.
'''

def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        # Crie uma flag que será usada para indicar se uma troca foi feita ou não
        troca = False

        # Percorra todos os elementos da lista
        for j in range(0, n-i-1):
            # Se o elemento atual é maior que o próximo
            if lista[j] > lista[j+1] :
                # Realize a troca
                lista[j], lista[j+1] = lista[j+1], lista[j]
                # Indique que uma troca foi feita
                troca = True

        # Se não houve trocas na última passagem, a lista está ordenada
        if not troca:
            break

    return lista

# Teste a função
print(bubble_sort([5, 3, 8, 4, 2]))  # Saída: [2, 3, 4, 5, 8]

'''
Este código define uma função bubble_sort que aceita uma lista de números como entrada e retorna a lista ordenada. 
A função usa um loop for para percorrer cada elemento da lista. Se o elemento atual for maior que o próximo, ele troca os dois elementos. 
Se nenhum elemento foi trocado na última passagem, a função sabe que a lista está ordenada e termina o processo.
'''