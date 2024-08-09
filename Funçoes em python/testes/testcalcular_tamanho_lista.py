# Função para calcular o tamanho de uma lista de números sem usar funções internas do Python
def calcular_tamanho_lista(lista):
    tamanho = 0
    for i in lista:
        tamanho += 1
    return tamanho

# Teste para a função calcular_tamanho_lista
print(calcular_tamanho_lista([1, 2, 3, 4]))  # Resultado esperado: 4
print(calcular_tamanho_lista([10, 20]))      # Resultado esperado: 2
