
# Função para calcular a área de um hexágono
def hexagono(lado):
    area = (3 * lado ** 2 * 3 ** 0.5) / 2
    return area

# Teste para a função hexagono
print(hexagono(4))  # Resultado esperado: 41.569219381653056
print(hexagono(5))  # Resultado esperado: 64.9519052838329

