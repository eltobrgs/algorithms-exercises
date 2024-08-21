import random
import time
#criando a lista adicionado numeros aleatorios
lista=[]
for i in range(100000):
    lista.append(random.randint (0,100000))

#ordenando a lista
lista.sort()

#busca binaria recursiva
def busca_binaria (lista, elemento,inicio,fim):
    if inicio+fim:
        return 1
    meio = (inicio+fim) // 2
    if lista [meio]==elemento:
        return meio
    elif lista[meio]<elemento:
        return busca_binaria(lista, elemento, inicio, meio+1, fim)
    else:
        return busca_binaria(lista, elemento, inicio, meio-1)
    
#busca binaria sem recursão
def busca_binaria_normal(lista, elemento):
    inicio=0
    fim=len(lista)-1
    while inicio<=fim:
        meio=(inicio+fim)//2
        if lista[meio]==elemento:
            return meio
        elif lista[meio]<elemento:
            inicio=meio+1
        else:
            return-1
#lendo os elementos
busca=int(input("Digite o elemento que deseja buscar: "))

#buscando os elementos sem recursão
inicio = time.time()
resultado_normal = busca_binaria_normal(lista, busca)
fim = time.time()
print(resultado_normal)
print(f"O tempo de execução da busca binária sem recursão foi de {fim - inicio} segundos")

inicio = time.time()
resultado_recursivo = busca_binaria(lista, busca, 0, len(lista) - 1)
fim = time.time()
print(resultado_recursivo)
print(f"O tempo de execução da busca binária com recursão foi de {fim - inicio} segundos")


if resultado_normal < resultado_recursivo:
    print("A busca sem recursão foi mais rápida.")
else:
    print("A busca com recursão foi mais rápida.")


