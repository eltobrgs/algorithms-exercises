# Calcular a moda
contador = {}
lista_numeros = list(range(1, 21))

for numero in lista_numeros:
    if numero in contador:
        contador[numero] += 1
    else:
        contador[numero] = 1

moda = None
max_count = 0
for numero, count in contador.items():
    if count > max_count:
        moda = numero
        max_count = count

print("A moda dos elementos na lista é:", moda)

# Calcular a mediana
lista_ordenada = sorted(lista_numeros)
tamanho = len(lista_ordenada)

if tamanho % 2 == 0:
    indice1 = tamanho // 2 - 1
    indice2 = tamanho // 2
    mediana = (lista_ordenada[indice1] + lista_ordenada[indice2]) / 2
else:
    indice = tamanho // 2
    mediana = lista_ordenada[indice]

print("A mediana dos elementos na lista é:", mediana)

# Calcular a média
soma = sum(lista_numeros)
media = soma / len(lista_numeros)
print("A média dos elementos na lista é:", media)
