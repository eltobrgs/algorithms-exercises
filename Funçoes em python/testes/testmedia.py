def calcular_tamanho_lista(lista): #funçao necessaria para calcular a media
    tamanho = 0
    for i in lista:
        tamanho += 1
    return tamanho

def calcular_soma(numeros): #funçao necessaria para calcular a media
    soma = 0
    for num in numeros:
        soma += num
    return soma

# Função para calcular a média de números em uma lista
def calcular_media(numeros):
    soma = calcular_soma(numeros)
    media = soma / calcular_tamanho_lista(numeros)
    return media

# Teste para a função calcular_media
print(calcular_media([10, 20, 30]))  # Resultado esperado: 20.0
print(calcular_media([5, 5, 5]))     # Resultado esperado: 5.0